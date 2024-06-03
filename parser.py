import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
import asyncio


def match():
    pass


def format_date(date_all):
    date = re.findall(r"\d{2}[.]\d{2}[.]\d{4}", date_all)
    if len(date) == 2:
        start_date = date[0]
        finish_date = date[-1]
    else:
        start_date = date[0]
        finish_date = date[0]
    time = re.findall(r"\d{2}[:]\d{2}", date_all)
    start_time = time[0]
    finish_time = time[-1]
    return [start_date, finish_date, start_time, finish_time]


def format_data(data):
    mask_subject = re.search(r"[(]\w*\s*\w*[)]", data)
    if type(mask_subject) == type(None):
        subject = "Undefined"
    else:
        subject = mask_subject.group()[1:-1]
    mask_tour = re.search(
        r"(Заключительный|Теоретический|Отборочный|Наблюдательный|Практический|II отборочный|Третий отборочный)(\s+)(этап|тур|раунд)",
        data,
    )
    if type(mask_tour) == type(None):
        tour = "Undefined"
    else:
        tour = mask_tour.group()
    mask_name = data.replace(tour, "").replace(subject, "")
    name = re.sub(r"[\(\)\-\–\–\_]*", "", mask_name).rstrip().replace("\u200b", "")

    return [subject, tour, name]


class Olympiad:
    def __init__(self, data, date):
        subject, tour, name = data
        start_date, finish_date, start_time, finish_time = date
        self.name = name
        self.tour = tour
        self.subject = subject
        self.start_date = start_date
        self.finish_date = finish_date
        self.start_time = start_time
        self.finish_time = finish_time
        self.link = ""
        self.university = ""
        self.level = -1

    def __str__(self) -> str:
        return f"name = {self.name}\n subject = {self.subject}\n tour = {self.tour}\n time = {self.start_date} - {self.finish_date} <> {self.start_time} - {self.finish_time}\n"

    def add_link(self, link) -> None:
        self.link = link
        return

    def add_level(self, level) -> int:
        self.level = level
        return

    def get_date(self) -> list:
        return [self.start_date, self.finish_date]

    def get_all_info(self):
        date_str1 = f"{self.start_date} {self.start_time}"
        date_str2 = f"{self.finish_date} {self.finish_time}"
        return {
            "name": self.name,
            "date_start": datetime.strptime(date_str1, "%d.%m.%Y %H:%M"),
            "date_end": datetime.strptime(date_str2, "%d.%m.%Y %H:%M"),
            "tour": self.tour,
            "subject": self.subject,
            "level": self.level,
            "link": self.link,
            "university": self.university,
        }


class Parser:
    def __init__(self):
        pass

    @classmethod
    async def get_month_olympiads(self, year, month):
        URL = f"https://postypashki.ru/ecwd_calendar/calendar/?date={year}-{month}-15&t=full"
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", class_="ecwd_calendar_container full cal_blue")
        events = (
            table.findAll("td", class_="day-with-date has-events")
            + table.findAll("td", class_="day-with-date weekend has-events")
            + table.findAll("td", class_="day-with-date week-start has-events")
        )
        events_unpacked = set()
        olympiad_lst = []
        for event_day in events:
            for event in event_day.findAll("li"):
                link = event.a.get("href")
                events_unpacked.add(link)
        for link in events_unpacked:
            r = requests.get(link)
            soup_olympiad = BeautifulSoup(r.text, "html.parser").find(
                "div", class_="ecwd-event"
            )
            olympiad_data = soup_olympiad.h1.text
            olympiad_date = soup_olympiad.find("span", class_="ecwd-event-date").text
            olympiad = Olympiad(format_data(olympiad_data), format_date(olympiad_date))
            olympiad_lst.append(olympiad.get_all_info())
        return olympiad_lst

    @classmethod
    async def get_year_olympiads(self, year=2024):
        olympiad_lst = []
        for month in range(1, 12):
            parsed_olimpiad = await self.get_month_olympiads(year, month)
            if len(parsed_olimpiad):
                olympiad_lst += parsed_olimpiad
            else:
                continue
        return olympiad_lst

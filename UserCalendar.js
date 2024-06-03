import React, {Fragment, useState} from "react";
import "./UserCalendar.css";
import { Info, DateTime, Interval } from "luxon";
import classnames from "classnames";
import AppCal from "./AppCal.tsx";

const Calendar = ({ meetings }) => {
    meetings = AppCal(100,  "2020-01-01T00:00:00", "2030-01-01T00:00:00")
    console.log(meetings);
    console.log(meetings["2024-04-26T00:00:00"]);
    const today = DateTime.local();
    console.log(today)
    const [activeDay, setActiveDay] = useState(null);
    const [firstDayOfActiveMonth, setFirstDayOfActiveMonth] = useState(
        today.startOf("month")
    );
    const activeDayMeetings = meetings[activeDay?.toISODate()] ?? [];
    const weekDays = Info.weekdays("short");
    const daysOfMonth = Interval.fromDateTimes(
        firstDayOfActiveMonth.startOf("week"),
        firstDayOfActiveMonth.endOf("month").endOf("week")
    )
        .splitBy({ day: 1 })
        .map((day) => day.start);
    const goToPreviousMonth = () => {
        setFirstDayOfActiveMonth(firstDayOfActiveMonth.minus({ month: 1 }));
    };
    const goToNextMonth = () => {
        setFirstDayOfActiveMonth(firstDayOfActiveMonth.plus({ month: 1 }));
    };
    const goToToday = () => {
        setFirstDayOfActiveMonth(today.startOf("month"));
    };

    return (
        <div className="calendar-container">
            <div className="calendar">
                <div className="calendar-headline">
                    <div className="calendar-headline-month">
                        {firstDayOfActiveMonth.monthShort}, {firstDayOfActiveMonth.year}
                    </div>
                    <div className="calendar-headline-controls">
                        <div
                            className="calendar-headline-control"
                            onClick={() => goToPreviousMonth()}
                        >
                            «
                        </div>
                        <div
                            className="calendar-headline-control calendar-headline-controls-today"
                            onClick={() => goToToday()}
                        >
                            Today
                        </div>
                        <div
                            className="calendar-headline-control"
                            onClick={() => goToNextMonth()}
                        >
                            »
                        </div>
                        <div
                            className="calendar-headline-control"
                            onClick={() => goToToday()}
                        >
                            Filter
                        </div>
                    </div>
                </div>
                <div className="calendar-weeks-grid">
                    {weekDays.map((weekDay, weekDayIndex) => (


                        <div key={weekDayIndex} className="calendar-weeks-grid-cell">
                            {weekDay}
                        </div>
                    ))}
                </div>
                <div className="calendar-grid">
                    {daysOfMonth.map((dayOfMonth, dayOfMonthIndex) => (
                        <div
                            key={dayOfMonthIndex}
                            className={classnames({
                                "calendar-grid-cell": true,
                                "calendar-grid-cell-has-events": Object.keys(meetings).includes(dayOfMonth.toISODate()) && dayOfMonth.month === firstDayOfActiveMonth.month,
                                "calendar-grid-cell-inactive-has-events": Object.keys(meetings).includes(dayOfMonth.toISODate()) && dayOfMonth.month !== firstDayOfActiveMonth.month,
                                "calendar-grid-cell-inactive":
                                    dayOfMonth.month !== firstDayOfActiveMonth.month,
                                "calendar-grid-cell-active":
                                    activeDay?.toISODate() === dayOfMonth.toISODate(),
                            })}
                            onClick={() => setActiveDay(dayOfMonth)}
                        >
                            {dayOfMonth.day}
                        </div >
                    ))}
                </div>
            </div>


            <div className="schedule">
                <div className="schedule-headline">
                    {activeDay === null && <div>Please select a day</div>}
                    {activeDay && (
                        <div>{activeDay.toLocaleString(DateTime.DATE_MED)}</div>
                    )}
                </div>
                <div>
                    {activeDay && activeDayMeetings.length === 0 && (
                        <div>No Planned Meetings Today1</div>
                    )}
                    {activeDay && activeDayMeetings.length > 0 && (
                        <>
                            {activeDayMeetings.map((meeting, meetingIndex) => (
                                <div key={meetingIndex}>
                                    <Fragment>
                                        <div>
                                            Name: {meeting.name}
                                        </div>
                                        <div>
                                            Subject: {meeting.subject}
                                        </div>
                                        <div>
                                            Level: {meeting.number}
                                        </div>
                                        <div>
                                            Tour: {meeting.tour}
                                        </div>
                                        <div>
                                            Link: {meeting.link}
                                        </div>
                                        <div>
                                            University: {meeting.university}
                                        </div>
                                        <div>
                                            Start: {meeting.date_start}
                                            {meeting.date_end.slice(8,10) - today.day}
                                        </div>
                                        <div>
                                            End: {meeting.date_end}
                                        </div>
                                        <br />
                                        {Number((meeting.date_end.slice(8,10)) - today.day) >= 0 &&
                                            <div className='card'>
                                                {meeting.name}
                                                <br/>
                                                {meeting.link}
                                            </div>
                                        }
                                    </Fragment>
                                </div>
                            ))}
                        </>
                    )}
                </div>
            </div>
        </div>
    );
};

export default Calendar;

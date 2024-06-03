import { useEffect, useState } from 'react';
import axios from 'axios';


interface Event {
    name: string;
    subject: string;
    level: number;
    tour: string;
    link: string;
    university: string;
    date_start: string;
    date_end: string;
}

const AppCal = (limit=100, event_date_start = "2020-01-01T00:00:00", event_date_end = "2030-01-01T00:00:00") => {
    const [eventsByDate, setEventsByDate] = useState<{
        [key: string]: Event[];
    }>({});
    const [requestBody] = useState({
        limit,
        event_date_start,
        event_date_end}
    );
    useEffect(() => {
        const fetchEvents = async () => {
            try {

                const response = await axios.post('http://127.0.0.1:9000/users/filter_events', requestBody);
                const events: Event[] = response.data;
                const newEventsByDate: { [key: string]: Event[] } = {};
                events.forEach((event) => {
                    const ISOdate = new Date(event.date_start).toISOString().split("T")[0];
                    if (!newEventsByDate[ISOdate]) {
                        newEventsByDate[ISOdate] = [];
                    }
                    newEventsByDate[ISOdate].push(event);
                });
                setEventsByDate(newEventsByDate);
            } catch (error) {
                console.error(error);
            }
        };
        fetchEvents();
    }, [requestBody]);

    return eventsByDate;}
export default AppCal;

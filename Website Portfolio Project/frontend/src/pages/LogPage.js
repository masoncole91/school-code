import React, {useState, useEffect} from "react";
import {useNavigate} from "react-router-dom";
import {MdNoteAdd} from "react-icons/md";

import TableHead from '../components/TableHead.js';

function LogPage({setEvent}) {
    const redirect = useNavigate();

    const [events, setEvents] = useState([]);

    const loadEvents = async () => {
        const response = await fetch("/log");
        const events = await response.json();
        setEvents(events);
    } 

    const onEditEvent = async event => {
        setEvent(event);
        redirect("/edit-event");
    }

    const onDeleteEvent = async _id => {
        const response = await fetch(`/log/${_id}`, {method: "DELETE" });
        if (response.status === 204) {
            const getResponse = await fetch("/log");
            const events = await getResponse.json();
            setEvents(events);
        } else {
            console.error(`Failed to delete event with _id = ${_id}, status code = ${response.status}`)
        }
    }

    useEffect(() => {
        loadEvents();
    }, []);

    return (
        <>
            <h2>Study Sessions <MdNoteAdd onClick={() => redirect("/add-event")} class="inline-button" /></h2>
            <p>Below is a log of the topics I've studied, how long I've studied them, and when I studied.</p>
            <p>Click <MdNoteAdd /> above to add a new session.</p>
            <TableHead 
                events={events}
                onEdit={onEditEvent}
                onDelete={onDeleteEvent} 
            />
        </>
    );
}

export default LogPage;
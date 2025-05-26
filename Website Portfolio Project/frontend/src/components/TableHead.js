import React from "react";
import LogRow from "./LogRow";

function TableHead({events, onEdit, onDelete}) {
    return (
        <table id="events">
            <caption>Study Log</caption>
            <thead>
                <tr>
                    <th>Topic</th>
                    <th>Time Spent</th>
                    <th>Date</th>
                    <th>Edit</th>
                    <th>Delete</th>
                </tr>
            </thead>
            <tbody>
                {events.map((event, e) => 
                    <LogRow
                        event={event} 
                        key={e}
                        onEdit={onEdit}
                        onDelete={onDelete}
                    />)}
            </tbody>
        </table>
    );
}

export default TableHead;
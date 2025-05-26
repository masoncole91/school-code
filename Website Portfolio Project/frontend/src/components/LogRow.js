import React from "react";
import {MdDelete, MdEdit} from "react-icons/md";

function LogRow({event, onEdit, onDelete}) {
    return(
        <tr>
            <td class="table-button">{event.topic}</td>
            <td class="table-button">{event.time} hours</td>
            <td class="table-button">{event.date.slice(0,10)}</td>
            <td class="table-button"><MdEdit onClick={() => onEdit(event)} id="table-button" class="inline-button"/></td>
            <td class="table-button"><MdDelete onClick={() => onDelete(event._id)} id="table-button" class="inline-button"/></td>
        </tr>
    );
}

export default LogRow;
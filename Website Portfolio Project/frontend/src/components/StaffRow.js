import React from "react";

function StaffRow({ person }) {
  return (
    <tr>
      <td>
        <img src={person.picture.thumbnail} class="random" alt="" />
      </td>
      <td>
        <a href="mailto:{person.email}">
          {person.name.first} {person.name.last}
        </a>
      </td>
      <td>{person.phone}</td>
      <td>{person.location.city}</td>
    </tr>
  );
}

export default StaffRow;

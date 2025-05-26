import React, { useState } from "react";
import StaffRow from "../components/StaffRow.js";

function StaffPage() {
  const [results, setResults] = useState([]);
  const fetchResults = () => {
    fetch("https://randomuser.me/api/?results=10")
      .then((response) => response.json())
      .then((response) => {
        setResults(response.results);
      })
      .catch(() => {
        alert("Not working.");
      });
  };
  return (
    <div>
      <h2>Staff</h2>
      <article>
        <p>
          The table below dynamically generates row content with a{" "}
          <strong>Document Object Model</strong> for the{" "}
          <a href="https://randomuser.me/" target="_blank" rel="noreferrer">
            Random User Generator
          </a>
          . This API creates a random person with contact data by calling to the
          browser with an <strong>async</strong> function,{" "}
          <strong>event listener</strong>, and <strong>try</strong> and{" "}
          <strong>catch</strong> methods. Another way is calling to the server
          with <strong>asyncHandler</strong>, <strong>await</strong>,{" "}
          <strong>fetch</strong>, and <strong>res.send</strong> methods. Both
          routes use <strong>innerHTML</strong>, a DOM model that lets
          JavaScript access and modify HTML content.
        </p>
        <button
          id="fromBrowser"
          onClick={fetchResults}
          value="Call from the browser."
        >
          Generate
        </button>
        <table class="random">
          <caption class="random">Either button above generates staff.</caption>
          <thead>
            <tr>
              <th>Portrait</th>
              <th>Name/Email</th>
              <th>Telephone</th>
              <th>City</th>
            </tr>
          </thead>
          <tbody id="personData" class="random">
            {results.map((person, indice) => (
              <StaffRow person={person} key={indice} />
            ))}
          </tbody>
        </table>
      </article>
    </div>
  );
}

export default StaffPage;

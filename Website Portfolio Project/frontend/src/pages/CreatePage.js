import React, {useState} from "react";
import {useNavigate} from "react-router-dom";

export const CreatePage = () => {

  const [topic, setTopic] = useState("");
  const [time, setTime] = useState("");
  const [date, setDate] = useState("");

  const redirect = useNavigate();

  const addEvent = async () => {
    const newEvent = {topic, time, date};

    const response = await fetch("/log", {
      method: "post",
      body: JSON.stringify(newEvent),
      headers: {"Content-Type": "application/json",},
    });

    if (response.status === 201) {
      alert("event added");
      redirect("/log");
    } else {
      alert(`failed to add event. code: ${response.status}`);
    }
  };

  return (
    <>
    <article>
      <h2>Study Log</h2>
      <p>Log your topic you've studied below.</p>
      <form onSubmit={(e) => {e.preventDefault();}}>
      <fieldset>
      <legend>What did you study?</legend>

      <label for="topic">Topic</label>
      <input
        type="text" 
        placeholder="Chemistry" 
        value={topic}
        onChange={e => setTopic(e.target.value)}
        id="topic" 
        required />
      
      <label for="time">Time Spent (Hours)</label>
      <input
        type="number"
        min="0"
        max="24"
        placeholder="1 hour" 
        value={time}
        onChange={e => setTime(e.target.value)}
        id="time" 
        required />
      
      <label for="date">Date</label>
      <input
        type="date" 
        placeholder={Date.now}
        value={date}
        onChange={e => setDate(e.target.value)}
        id="date" 
        required />
      
      <label for="submit">
        <button
          type="submit"
          onClick={addEvent}
          id="submit"
          >Submit</button></label>
    
    </fieldset>
    </form>
    </article>
    </>
  );
};

export default CreatePage;

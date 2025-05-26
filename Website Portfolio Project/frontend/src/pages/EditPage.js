import React, {useState} from "react";
import {useNavigate} from "react-router-dom";

export const EditPage = ({setEvent}) => {
  const [topic, setTopic] = useState(setEvent.topic);
  const [time, setTime] = useState(setEvent.time);
  const [date, setDate] = useState(setEvent.date);

  const redirect = useNavigate();

  const editEvent = async () => {
    const response = await fetch(`/log/${setEvent._id}`, {
      method: "PUT",
      body: JSON.stringify({
        topic: topic,
        time: time,
        date: date
      }),
      headers: {"Content-Type": "application/json",},
    });

    if (response.status === 200) {
        alert("edited success");
        redirect("/log")
    } else {
        const errorMessage = await response.json();
        alert(`failed ${response.status} ${errorMessage.Error}`);
        redirect("/");
    }
  };

  return (
    <>
    <article>
    <h2>Edit Log</h2>
    <p>Edit a study session below.</p>
    <form onSubmit={(e) => { e.preventDefault();}}>
                <fieldset>
                    <legend>Which session are you editing?</legend>
                    <label for="topic">Topic</label>
                    <input
                        type="text"
                        value={topic}
                        onChange={e => setTopic(e.target.value)} 
                        id="topic" 
                        required />
                    
                    <label for="time">Time Spent</label>
                    <input
                        type="number"
                        min="0"
                        max="24"
                        value={time}
                        onChange={e => setTime(e.target.value)} 
                        id="time" 
                        required />

                    <label for="date">Date</label>
                    <input
                        type="date"
                        value={date}
                        onChange={e => setDate(e.target.value)} 
                        id="date" 
                        required />

                    <label for="submit">
                    <button
                        type="submit"
                        onClick={editEvent}
                        id="submit"
                        >Save</button></label>
                </fieldset>
                </form>
            </article>
    </>
  );
};

export default EditPage;
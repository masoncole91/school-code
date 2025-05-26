import mongoose from "mongoose";
import "dotenv/config";

mongoose.connect(
    process.env.MONGODB_CONNECT_STRING,
    {useNewUrlParser: true}
);

const database = mongoose.connection;

database.once("open", (error) => {
    if(error){
        res.status(500).json({error: "database connection failure"});
    } else {
        console.log("database connection successful");
    }
});

const eventSchema = mongoose.Schema({
    topic: {type: String, required: true},
    time: {type: Number, required: true},
    date: {type: Date, required: true, default: Date.now}
});

const Event = mongoose.model("Event", eventSchema);

const createEvent = async (topic, time, date) => {
    const event = new Event({
        topic: topic,
        time: time,
        date: date
    });
    return event.save();
}

const findEvent = async () => {
    const query = Event.find();
    return query.exec();
}

const findEventById = async (id) => {
    const query = Event.findById(id);
    return query.exec();
}

const replaceEvent = async (id, topic, time, date) => {
    const result = await Event.replaceOne({_id: id}, {
        topic: topic,
        time: time,
        date: date
    });
    return { 
        id: id,
        topic: topic,
        time: time,
        date: date
    }
}

const deleteById = async (id) => {
    const result = await Event.deleteOne({_id: id});
    return result.deletedCount;
}

export {createEvent, findEvent, findEventById, replaceEvent, deleteById}
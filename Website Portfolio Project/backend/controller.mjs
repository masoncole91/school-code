import "dotenv/config";
import express from "express";
import * as eventdata from "./model.mjs";

const PORT = process.env.PORT;
const app = express();

app.use(express.json());

app.post("/log", (req, res) => {
    eventdata.createEvent(
        req.body.topic,
        req.body.time,
        req.body.date
    )
    .then(event => {
        res.status(201).json(event);
    })
    .catch(error => {
        console.log(error);
        res.status(400).json({error: "creation failed"})
    });
});

app.get("/log", (req, res) => {
    eventdata.findEvent()
    .then(event => {
        if (event !== null) {
            res.json(event);
        } else {
            res.status(404).json({Error: "not found"})
        }
    })
    .catch(error => {
        console.log(error);
        res.status(400).json({error: "retrieval failed"})
    });
});

app.put("/log/:id", (req, res) => {
    eventdata.replaceEvent(
        req.params.id,
        req.body.topic,
        req.body.time,
        req.body.date
    )
    .then(event => {
        res.json(event);
    })
    .catch(error => {
        console.log(error);
        res.status(400).json({error: "replace failed"})
    });
});

app.delete("/log/:id", (req, res) => {
    eventdata.deleteById(req.params.id)
    .then(deletedCount => {
        if (deletedCount === 1) {
            res.status(204).send();
        } else {res.status(404).json({error: "event doesn't exist"})
    }
    })
    .catch(error => {
        console.log(error);
        res.status(500).json({error: "deletion failed"});
    });
});

app.listen(PORT, () => {
    console.log(`listening at port ${PORT}`);
});
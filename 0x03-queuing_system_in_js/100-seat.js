import { createClient } from "redis";
import { createQueue } from "kue";
const express = require('express');
const { promisify } = require('util');
/* Managing the available seat in a meeting */
const client = createClient();
const key = 'available_seats';
const get = promisify(client.get).bind(client);
var reservationEnabled = true;
const app = express();
const port = 1245;
const queue = createQueue();

app.use(express.json())

client.on('error', (err) => {
    console.log(`Client redis not connected: ${err}`);
});

function reserveSeat(number) {
    client.set(key, number);
}

async function getCurrentAvailableSeats() {
    const availableSeats = await get(key);
    return parseInt(availableSeats, 10) || 0;
}
reserveSeat(50);

app.get('/available_seats', async (req, res) => {
    const available_seats = await getCurrentAvailableSeats();
    res.json({
        numberOfAvailableSeats: available_seats
    })
})

app.get('/reserve_seat', (req, res) => {
    if (!reservationEnabled) {
        res.json({ status: 'Reservation are blocked' })
    }
    else {
        const job = queue.create('reserve_seat')
            .save((err) => {
                if (!err) res.json({ status: 'Reservation in process' });
                else res.json({ status: 'Reservation failed' });
            });
        job.on('complete', () => {
            console.log(`Seat reservation job ${job.id} completed`);
        });
        job.on('failed', (err) => {
            console.log(`Seat reservation job ${job.id} failed: ${err}`);
        });

    }
})

app.get('/process', async (req, res) => {
    res.json({ status: 'Queue processing' });

    queue.process('reserve_seat', async (job, done) => {
        const seats = await getCurrentAvailableSeats();
        if (seats > 0) reserveSeat(key, seats - 1);
        if (seats - 1 === 0) reservationEnabled = false;
        if (seats - 1 >= 0) done();
        else done(new Error('Not enough seats available'));
    });

})

app.listen(port, () => {
    console.log(`Express server is running on the port: ${port}`);
})


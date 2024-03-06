const express = require('express');
const { promisify } = require('util');
const redis = require('redis');
const kue = require('kue');

const app = express();
const port = 1245;

// Redis client
const client = redis.createClient();
const reserveSeatAsync = promisify(client.set).bind(client);
const getCurrentAvailableSeatsAsync = promisify(client.get).bind(client);

// Kue queue
const queue = kue.createQueue();

// Initialize available seats and reservation status
let availableSeats = 50;
let reservationEnabled = true;

// Reserve a seat function
const reserveSeat = async (number) => {
    await reserveSeatAsync('available_seats', number);
};

// Get current available seats function
const getCurrentAvailableSeats = async () => {
    const seats = await getCurrentAvailableSeatsAsync('available_seats');
    return parseInt(seats) || 0;
};

// Server
app.listen(port, () => {
    console.log(`Server is listening on port ${port}`);
});

// Routes
app.get('/available_seats', async (req, res) => {
    const numberOfAvailableSeats = await getCurrentAvailableSeats();
    res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservation are blocked' });
    }
    const job = queue.create('reserve_seat').save((err) => {
        if (err) {
            return res.json({ status: 'Reservation failed' });
        }
        res.json({ status: 'Reservation in process' });
    });
    job.on('complete', (result) => {
        console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (errorMessage) => {
        console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
    });
});

app.get('/process', async (req, res) => {
    res.json({ status: 'Queue processing' });
    queue.process('reserve_seat', async (job, done) => {
        const currentAvailableSeats = await getCurrentAvailableSeats();
        if (currentAvailableSeats === 0) {
            reservationEnabled = false;
        }
        if (currentAvailableSeats >= 1) {
            await reserveSeat(currentAvailableSeats - 1);
            done();
        } else {
            done(new Error('Not enough seats available'));
        }
    });
});

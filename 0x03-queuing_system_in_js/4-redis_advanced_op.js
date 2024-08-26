import { createClient } from "redis";
const redis = require('redis');
const redisClient = createClient();

function createHset() {
    const hkey = "HolbertonSchools";
    const hvalues = {
        "Portland": 50,
        "Seattle": 80,
        "New York": 20,
        "Bogota": 20,
        "Cali": 40,
        "Paris": 2
    }
    for (const [field, value] of Object.entries(hvalues)) {
        redisClient.hset(hkey, field, value, redis.print);
    }
}

function displayHset() {
    const hkey = "HolbertonSchools";
    redisClient.hgetall(hkey, (err, reply) => {
        console.log(reply);
    })
}

createHset();
displayHset();

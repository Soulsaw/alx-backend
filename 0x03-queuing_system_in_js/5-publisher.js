import { createClient } from "redis";
/* Using the publisher featue in redis */
const redisClient = createClient();

redisClient.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
redisClient.on('ready', () => console.log(`Redis client connected tot the server`));

function publishMessage(message, time) {
    const channel = 'holberton school channel';
    setTimeout(() => {
        redisClient.publish(channel, message)
        console.log(`About to send ${message}`);
    }, time);
}
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);

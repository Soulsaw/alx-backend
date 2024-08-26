import { createClient } from "redis";

const redisClient = createClient();

redisClient.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
redisClient.on('ready', () => console.log(`Redis client connected tot the server`));

const channel = 'holberton school channel';

redisClient.subscribe(channel, ()=>{});

redisClient.on('message', (_, msg) =>{
    if (msg === 'KILL_SERVER'){
        redisClient.unsubscribe();
        redisClient.quit();
    }
    console.log(`${msg}`);
});

import { createClient, print } from "redis";
/* Set a value in the redis server */
const redisClient = createClient();

redisClient.on('error', (err) => { console.log(`Redis client not connected to the server: ${err}`) });
redisClient.on('ready', () => { console.log(`Redis client connected to the server`) });

function setNewSchool(schoolName, value) {
    redisClient.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
    redisClient.get(schoolName, (err, reply) => {
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

const kue = require('kue');
const queue = kue.createQueue();

function sendNotification(phoneNumber, message){
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
const job = queue.process('push_notification_code', sendNotification(4153518780, 'This is the code to verify your account'));

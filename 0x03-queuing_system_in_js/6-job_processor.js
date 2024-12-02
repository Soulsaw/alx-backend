import { createQueue } from "kue";
/* Job processor with "kue" */
const queue = createQueue();

function sendNotification(phoneNumber, message){
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
queue.process('push_notification_code', (job, _)=>{
    const {phoneNumber, message} = job.data;
    sendNotification(phoneNumber, message);
});

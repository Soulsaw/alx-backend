import { createQueue } from "kue";
/* Job creator in redis server */
const queue = createQueue();

const jobData = {
    phoneNumber: "4153518780",
    message: "This is the code to verify your account"
}
const job = queue.create('push_notification_code', jobData);
job.save(() => {
    console.log(`Notification job created: ${job.id}`);
});
job.on('complete', () => {
    console.log(`Notification job completed`);
});
job.on('failed', () => {
    console.log(`Notification job failed`);
});


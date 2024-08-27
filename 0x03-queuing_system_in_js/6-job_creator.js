const kue = require('kue');
const queue = kue.createQueue();
const data = {
    phoneNumber: String,
    message: String
}
const job = queue.create('push_notification_code', data);
job.save(()=>{
    console.log(`Notification job created: ${job.id}`);
});
job.on('complete', ()=>{
    console.log(`Notification job completed`);
});
job.on('failed', ()=>{
    console.log(`Notification job failed`);
});

import { createQueue } from "kue";
/* Job processor again */
const queue = createQueue();

const blackListPhoneNumbers = ['4153518780', '4153518781'];

queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
});

function sendNotification(phoneNumber, message, job, done) {
    job.progress(0, 100);
    if (blackListPhoneNumbers.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw new Error('Jobs is not an array');
    }
    jobs.map((elem) => {
        const job = queue.create('push_notification_code_3', elem)
            .save(() => {
                console.log(`Notification job created: ${job.id}`);
            })
            .on("complete", () => {
                console.log(`Notification job ${job.id} completed`);
            })
            .on('error', (err) => {
                console.log(`Notification job ${job.id} failed: ${err}`);
            })
            .on('progress', (progress, _) => {
                console.log(`Notification job ${job.id} ${progress}% complete`);
            });
    });

}
module.exports = createPushNotificationsJobs;

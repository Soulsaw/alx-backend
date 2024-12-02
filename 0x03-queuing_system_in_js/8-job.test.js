import { expect } from "chai";
import createPushNotificationsJobs from "./8-job";
import { createQueue } from "kue";
/* unittest on job que */
const queue = createQueue();

before(function (done) {
    queue.testMode.enter(true);
    done();
});

afterEach(function () {
    queue.testMode.clear();
});

after(function () {
    queue.testMode.exit()
})
describe('createPushNotificationsJobs', () => {
    it('tess', (done) => {
        const list = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4153518786',
                message: 'This is the code 12654 to verify your account'
            }
        ];
        createPushNotificationsJobs(list, queue);
        queue.testMode.jobs('push_notification_code_3', function (err, jobs) {
            if (err) return done(err);
            expect(jobs).to.have.lengthOf(list.length);
            done();
        });
    })
})

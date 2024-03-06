import kue from 'kue';

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach(job => {
    if (!job.phoneNumber || !job.message) {
      throw new Error('Invalid job format: missing phoneNumber or message');
    }

    const pushNotificationJob = queue.create('push_notification_code_3', job).save(err => {
      if (err) {
        console.error(`Notification job ${pushNotificationJob.id} failed: ${err}`);
      } else {
        console.log(`Notification job created: ${pushNotificationJob.id}`);
      }
    });

    pushNotificationJob.on('complete', () => {
      console.log(`Notification job ${pushNotificationJob.id} completed`);
    });

    pushNotificationJob.on('failed', err => {
      console.error(`Notification job ${pushNotificationJob.id} failed: ${err}`);
    });

    pushNotificationJob.on('progress', (progress, data) => {
      console.log(`Notification job ${pushNotificationJob.id} ${progress}% complete`);
    });
  });
}

export default createPushNotificationsJobs;


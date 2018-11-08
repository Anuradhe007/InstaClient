import schedule
import time

class ClientScheduler:

    def job(self):
        print("I'm working...")

    def jobScheduler(self, timeToRun, job):
        schedule.every(timeToRun).seconds.do(job)
        # schedule.every(10).minutes.do(job)
        # schedule.every().hour.do(job)
        # schedule.every().day.at("10:30").do(job)

        while 1:
            schedule.run_pending()
            time.sleep(1)

clientScheduler = ClientScheduler()
clientScheduler.jobScheduler(5, clientScheduler.job)
#pip install schedule
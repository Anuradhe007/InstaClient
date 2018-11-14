import schedule
import time

class ClientScheduler:

    def __init__(self, time1, proxyPath, filesPath, credentials):
        self.time1 = time1
        self.proxyPath = proxyPath
        self.filesPath = filesPath
        self.credentials = credentials

    def job(self):
        print(self.time1.get().strip())
        print(self.proxyPath.get().strip())
        print(self.filesPath.get().strip())
        print(self.credentials)

    def jobScheduler(self, timeToRun, job):
        schedule.every(timeToRun).seconds.do(job)
        # schedule.every(10).minutes.do(job)
        # schedule.every().hour.do(job)
        # schedule.every().day.at("10:30").do(job)

        while 1:
            schedule.run_pending()
            time.sleep(1)

    def schedulerInitialize(self):
        self.jobScheduler(int(self.time1.get().strip()), self.job)

#pip install schedule
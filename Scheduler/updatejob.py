from apscheduler.schedulers.background import BackgroundScheduler
from Scheduler.Task1 import simulatejob

def start():
    scheduler=BackgroundScheduler()
    scheduler.add_job(simulatejob,trigger='cron', day_of_week='mon-sun', hour='17', minute='54',id="1",replace_existing=True)
    scheduler.start()
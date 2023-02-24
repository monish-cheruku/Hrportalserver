from apscheduler.schedulers.background import BackgroundScheduler
from Scheduler.Task1 import ManageADUsers

def start():
    scheduler=BackgroundScheduler()
    scheduler.add_job(ManageADUsers,trigger='cron', day_of_week='mon-sun', hour='*', minute='26',id="1",replace_existing=True)
    scheduler.start()
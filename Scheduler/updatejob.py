from apscheduler.schedulers.background import BackgroundScheduler
from Scheduler.Task1 import ManageADUsers, sendAccountCreationEmail

def start():
    scheduler=BackgroundScheduler()
    scheduler.add_job(ManageADUsers,trigger='cron', day_of_week='mon-sun', hour='*', minute='58',id="1",replace_existing=True)
    scheduler.add_job(sendAccountCreationEmail,trigger='cron', day_of_week='mon-sun', hour='*', minute='21',id="2",replace_existing=True)
    scheduler.start()
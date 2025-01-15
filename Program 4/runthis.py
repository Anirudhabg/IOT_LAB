from crontab import CronTab

my_cron = CronTab(user="pi4")
job = my_cron.new(
    command="python3/home/.....path...../"
)  # give the path of plaground.py
print("...Scheduling...")
job.minute.every(1)
my_cron.write()

#Switch on relay at a given time using cron, where the relays contact terminals are connected to load
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

relay = 38
GPIO.setup(relay,GPIO.OUT,initial = 0)

try:
    GPIO.output(relay,True)
    print("Relay is on press ctrl + c to close")
    time.sleep(5)
    GPIO.output(relay,False)
    print("Relay is off")
except:
    GPIO.cleanup()
    print("Exit")

from crontab import CronTab
my_cron = CronTab(user = "pi4")
job = my_cron.new(command = "python3/home/.....path...../")
print("...Scheduling...")
job.minute.every(1)
my_cron.write()
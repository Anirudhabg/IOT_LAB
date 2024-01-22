#Flash an LED at a given on time and off time cycle where the two times are taken form a file

import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led = 15

GPIO.setup(led,GPIO.OUT, initial = 0)

file = open("time.txt","r")
line = file.readlines()

on_time = int(line[0].split("=")[1])
off_time = int(line[1].split("=")[1])

try:
    GPIO.output(led,False)
    print("LED IS ON")
    time.sleep(on_time)
    GPIO.output(led,True)
    print("LED IS OFF")
    time.sleep(off_time)
except:
    GPIO.cleanup()

    

# Flash an LED at a given on time and off time cycle where the two times are taken form a file

import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led1 = 15
led2 = 13


GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)


file = open("time.txt", "r")
line = file.readlines()

on_time = int(line[0].split("=")[1])
off_time = int(line[1].split("=")[1])

counter = 0
try:
    while True:
        GPIO.output(led1, False)
        GPIO.output(led2, True)
        print("LED IS ON")
        time.sleep(on_time)
        GPIO.output(led1, True)
        GPIO.output(led2, False)
        print("LED IS OFF")
        time.sleep(off_time)
        counter += 1
        if counter == 10:
            break
    print("Exit")
except:
    GPIO.cleanup()

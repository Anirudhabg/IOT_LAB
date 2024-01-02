# 7 -> Print current time for 10 times with an interval of 10 seconds
import time


for i in range(10):
    currTime = time.strftime("%H:%M:%S")
    print("Current time: ",currTime)
    time.sleep(10)
#Using pi camera

from picamera import PiCamera
from time import sleep
import datetime

cam = PiCamera()
cam.start_preview()
curr_date = datetime.datetime.now().strftime('%Y - %m - %d %H : %M : %S')
sleep(3)
cam.capture('Path to folder where you want to save the image'+curr_date+'.jpg')
cam.stop_preview()

print("Image Captured")

# Note
# You should shutdown pc when inserting the camera module to Raspberry Pi and  before removing the module 
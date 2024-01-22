import time
import RPi.GPIO as gpio 

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

led_one = 15
led_two = 13

switch_one = 37
switch_two = 35

gpio.setup(led_one, gpio.OUT)
gpio.setup(switch_one, gpio.IN)
gpio.setup(led_two, gpio.OUT)
gpio.setup(switch_two, gpio.IN)

def glow_led(event):
    print(event)
    if event == switch_one:
        gpio.output(led_one,False)
        time.sleep(3)
        gpio.output(led_one,True)
    else:
        gpio.output(led_two,False)
        time.sleep(3)
        gpio.output(led_two,True)

gpio.add_event_detect(switch_one, gpio.RISING, callback = glow_led)
gpio.add_event_detect(switch_two, gpio.RISING, callback = glow_led)

try:
    while True:
        time.sleep(3)
except KeyboardInterrupt:
    gpio.cleanup()
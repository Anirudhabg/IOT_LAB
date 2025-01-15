# Get input from two switches and switch on corresponding LEDs
import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

led_one = 15
led_two = 13

switch_one = 37
switch_two = 35

# Defining Output
gpio.setup(led_one, gpio.OUT)
gpio.setup(led_two, gpio.OUT)

# Defining Input
gpio.setup(switch_one, gpio.IN)
gpio.setup(switch_two, gpio.IN)


def glow_led(event):
    print(event)
    if event == switch_one:
        gpio.output(led_one, False)  # LED is ON
        time.sleep(3)
        gpio.output(led_one, True)  # LED is OFF
    else:
        gpio.output(led_two, False)  # LED is ON
        time.sleep(3)
        gpio.output(led_two, True)  # LED is OFF


gpio.add_event_detect(switch_one, gpio.RISING, callback=glow_led)  # Event Handler
gpio.add_event_detect(switch_two, gpio.RISING, callback=glow_led)  # Event Handler

try:
    while True:
        time.sleep(3)
except KeyboardInterrupt:
    gpio.cleanup()

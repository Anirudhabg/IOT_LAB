#Get an alarm from a remote area (through LAN) if smoke is detected
#Client Side
import socket
import RPi.GPIO as GPIO
import time

HOST = '' #copy it from server side
PORT = 5000

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36,GPIO.OUT)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        while True:
            data = s.recv(1024).decode('utf-8')
            print(data)
            if str(data) == 'Alert':
                print('Gas Leakage Detected')
                GPIO.output(36,True)
                time.sleep(3)
                GPIO.output(36,False)
                time.sleep(3)
except:
    s.close()
    GPIO.cleanup()

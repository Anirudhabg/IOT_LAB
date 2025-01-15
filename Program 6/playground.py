# Program to control light using webpage

from flask import Flask, render_template
import time, datetime
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led = 15
GPIO.setup(led, GPIO.OUT)

app = Flask(__name__)


@app.route("/")
def hello():
    GPIO.output(led, True)
    return render_template("index.html")


@app.route("/ledon")
def ledOn():
    now = datetime.datetime.now()
    t = now.strftime("%Y - %m - %d %H : %M")
    d = {"Status": "ON", "Time": t}
    GPIO.output(led, False)
    return render_template("about.html", **d)


if __name__ == "__main__":
    app.run(debug=True)

try:
    while True:
        time.sleep(3)
except:
    GPIO.cleanup()

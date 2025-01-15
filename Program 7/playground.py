# Implement an intruder system that sends an alert to the given email
import RPi.GPIO as GPIO
import smtplib
from email.mime.text import MIMEText
from time import sleep

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_email_password"
RECEIVER_EMAIL = "receiver_email@gmail.com"

# PIR Sensor GPIO Pin
PIR_PIN = 17

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)


def send_email():
    """Function to send an email alert."""
    try:
        subject = "Intruder Alert!"
        body = "Motion detected! Check your surroundings immediately."
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL

        # Establish connection to the email server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
            print("Alert email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


try:
    print("Intruder alert system is active. Waiting for motion...")
    while True:
        if GPIO.input(PIR_PIN):  # Motion detected
            print("Motion detected!")
            send_email()
            sleep(10)  # Delay to avoid multiple alerts in quick succession
        sleep(1)  # Check for motion every second
except KeyboardInterrupt:
    print("System shutting down...")
finally:
    GPIO.cleanup()

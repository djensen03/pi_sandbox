import RPi.GPIO as GPIO
import time

readPIN = 31

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(readPIN, GPIO.IN)
GPIO.setwarnings(True)

print("Read: " + str(GPIO.input(readPIN)))
time.sleep(1)

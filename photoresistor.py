import RPi.GPIO as GPIO
import time
from bottle import run
readPIN = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(readPIN, GPIO.IN)
GPIO.setwarnings(True)

def read_LPR(readPIN):
    print("Read: " + str(GPIO.input(readPIN)))
    time.sleep(1)

try:
    print("I'm here")
    while True:
        read_LPR(readPIN)
finally:
    print('Cleaning up GPIO')
    GPIO.cleanup()
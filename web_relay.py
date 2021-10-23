from bottle import route, run, template, request
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin1 = 18
pin2 = 15
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

@route('/') 
def index():
    return template('home.tpl')
    
@route('/pin1_on')
def index():
    GPIO.output(pin1, True)
    return template('off.tpl')
    
@route('/pin1_off')
def index():
    GPIO.output(pin1, False)
    return template('off.tpl')


@route('/pin2_on')
def index():
    GPIO.output(pin2, True)
    return template('off.tpl')


@route('/pin2_off')
def index():
    GPIO.output(pin2, False)
    return template('off.tpl')

try:
    print("I'm here")
    run(host='0.0.0.0', port=83)
finally:  
    print('Cleaning up GPIO')
    GPIO.cleanup()

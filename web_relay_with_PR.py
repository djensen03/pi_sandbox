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

    if GPIO.input(pin2):
        return template('p1on_p2on.tpl')
    else:
        return template('p1on_p2off.tpl')


@route('/pin1_off')
def index():
    GPIO.output(pin1, False)
    if GPIO.input(pin2):
        return template('p1off_p2on.tpl')
    else:
        return template('home.tpl')


@route('/pin2_on')
def index():
    GPIO.output(pin2, True)
    if GPIO.input(pin1):
        return template('p1on_p2on.tpl')
    else:
        return template('p1off_p2on.tpl')


@route('/pin2_off')
def index():
    GPIO.output(pin2, False)
    if GPIO.input(pin1):
        return template('p1on_p2off.tpl')
    else:
        return template('home.tpl')

try:
    print("I'm here")
    run(host='0.0.0.0', port=83)
finally:  
    print('Cleaning up GPIO')
    GPIO.cleanup()

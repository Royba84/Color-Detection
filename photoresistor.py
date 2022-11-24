# This file deals with the LDR sensor & Flash light array
import RPI.GPIO as GPIO
import time
pr=8
led=7
# GPIO.setmode(GPIO.BOARD)  - Didn't work, changed to GPIO.BCM and it worked
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pr,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,GPIO.HIGH)

def read_photoresistor():
    if GPIO.input(pr)==1:
        GPIO.output(led,GPIO.HIGH)
    else:
            GPIO.output(led,GPIO.LOW)

read_photoresistor()

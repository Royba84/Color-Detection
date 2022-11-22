# This file handels with the Ultra-sonic distance sensor
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
trig=22
echo=23

GPIO.setwarnings(False)
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

GPIO.output(trig, GPIO.LOW)
print("wait for sensor...")
time.sleep(2)

def calc_distance():
    start=0
    end=0
    GPIO.output(trig,GPIO.HIGH)
    time.sleep(0.0001)
    GPIO.output(trig,GPIO.LOW)

    while GPIO.input(echo)==0:
        start=time.time()
    while GPIO.input(echo)==1:
        end=time.time()

        dur=end-start
        distance=round(dur*17150,2)
        return distance

    #END
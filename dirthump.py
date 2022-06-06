import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
# pump control pin setting
pumpcontrol_pin=19
GPIO.setup(pumpcontrol_pin,GPIO.OUT)
GPIO.setup(17,GPIO.IN)

#dirt humidity detect
def dirtdetect ():
        if GPIO.input(17)==False:
            #print('湿度适宜')
            pumpstart(False)
        elif GPIO.input(17)==True:
            #print('湿度低请浇水')
            pumpstart(True)

#pump start

def pumpstart(flag):
    if flag==True:
       GPIO.output(pumpcontrol_pin,GPIO.HIGH) #pump start when dirt humidity is low
    if flag==False:
       GPIO.output(pumpcontrol_pin,GPIO.LOW) #pump stop when dirt humidity is fit

#GPIO.output(19,False)
dirtdetect()
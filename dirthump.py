from difflib import diff_bytes
from pickle import TRUE
import re
import RPi.GPIO as GPIO
import time
import sys
GPIO.setwarnings (False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.IN)

# pump control pin setting
pumpcontrol_pin=18 
GPIO.setup(pumpcontrol_pin,GPIO.OUT)

#dirt humidity detect
def dirtdetect ():
        if GPIO.input(12)==False:
            print('湿度适宜')
            return False
        elif GPIO.input(12)==True:
            print('湿度低请浇水')
            return True

#pump start

def pumpstart(flag) :
    if flag==True:
       GPIO.output(pumpcontrol_pin,TRUE) #pump start when dirt humidity is low
    else :
       GPIO.output(pumpcontrol_pin,False) #pump stop when dirt humidity is fit 

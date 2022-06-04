import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
control_pin=18
GPIO.setup(control_pin,GPIO.OUT)
try:
     while True:
            GPIO.output(control_pin,1)
            time.sleep(5)
            GPIO.output(control_pin,0)
            time.sleep(2)
finally:
     print("Cleaning up")
     GPIO.cleanup()
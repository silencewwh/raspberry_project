import RPi.GPIO as GPIO
import time
def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.IN)
    GPIO.setup(26,GPIO.OUT)
    pass
def beep():
        for i in range(1,6):
            GPIO.output(26, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(26, GPIO.HIGH)
            time.sleep(0.5)
            print ("警告:有人靠近灌溉区域!")
def detct():
    for i in range(1, 31):
        if GPIO.input(16) == True:
            print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"监测到人体活动")
            beep()
        else:
            GPIO.output(26, GPIO.HIGH)#无人时关闭蜂鸣器
            print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"未监测到人体活动")
        time.sleep(3)
time.sleep(2)
init()
detct()
GPIO.cleanup()
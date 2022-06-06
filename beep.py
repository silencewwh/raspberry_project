import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.IN)
GPIO.setup(25,GPIO.OUT)

def beep():
        for i in range(1,3):
            GPIO.output(25, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(25, GPIO.HIGH)
            time.sleep(0.5)
            print ("警告:有人靠近灌溉区域!")
def detct():
    while True:
        if GPIO.input(24) == True:
            #print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"监测到人体活动")
            time.sleep(0.02)
            if GPIO.input(24)==True:
                beep()
        if GPIO.input(24)==False:
            GPIO.output(25, GPIO.HIGH)#无人时关闭蜂鸣器
            #print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+"未监测到人体活动")
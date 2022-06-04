from ast import Global
from asyncio import sleep
from difflib import diff_bytes
import RPI.GPIO as GPIO
import airpressure
import dirthump
import mqttclient
import sunlight
import tempdetect
import threading
import time

threadLock = threading.Lock()
threads=[]

airprs_data=0
dirthump_data=0
sunlight_data=0
temp_data=0
hump_data=0


class AThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print ("开启线程： " + self.name)
        threadLock.acquire()
        getdata(self.name, self.delay)
        threadLock.release()
       



#get data from raspberry pi
def getdata(ThreadName,delay):
    global airprs_data
    global dirthump_data
    global sunlight_data
    global temp_data
    global hump_data
    
    while True:
        airprs_data=airpressure.bmp280.getpressure()
        dirthump_data=dirthump.dirtdetect()
        sunlight_data=sunlight.getIlluminance()
        temp_data,hump_data=tempdetect.gettemp_and_hum()

        print(airprs_data+dirthump_data+sunlight_data+temp_data+hump_data)
        time.sleep(delay)

#upload data to mqtt broker
def uploaddata(TreadName,delay):
    while True:
        mqttclient.mqttupload()
        time.sleep(delay)






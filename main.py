import RPi.GPIO as GPIO
import airpressure
import beep
import dirthump
import mqttclient
import sunlight
import tempdetect
import threading
import time

airprs_data=0
dirthump_data=0
sunlight_data=0
temp_data=0
hump_data=0
mqttclient.mqttconnect()
   



#get data from raspberry pi
def getdata(delay):
    global airprs_data
    global dirthump_data
    global sunlight_data
    global temp_data
    global hump_data
    
    while True:
            airprs_data=round(airpressure.BMP180().getpressure()/1000,3)
            sunlight_data=sunlight.getIlluminance()
            temp_data,hump_data=tempdetect.gettemp_and_hum()
            #print(airprs_data,dirthump_data,sunlight_data,temp_data,hump_data)
            time.sleep(float(delay))

#upload data to mqtt broker
def uploaddata(delay):
    while True:
        mqttclient.mqttupload(airprs_data,dirthump_data,sunlight_data,temp_data,hump_data)
        time.sleep(float(delay))
        

def humandetect(delay):
    beep.detct()

def dirtandpump(delay):
    dirthump.dirtdetect()

if __name__=="__main__":
    T1=threading.Thread(target=uploaddata,args=("5",))
    T2=threading.Thread(target=getdata,args=("1",))
    T3=threading.Thread(target=humandetect,args=("1",))
    T4=threading.Thread(target=dirtandpump,args=("1",))
    T1.start()
    T2.start()
    T3.start()
    T4.start()
    #T1.join()
    #T2.join()
    #T3.join()
    #T4.join()




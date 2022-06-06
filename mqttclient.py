import paho.mqtt.client as mqtt
import time
import numpy as np
import sys
import random

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected with result code {rc}")
    else:
        print("failed to connect,return code%d\n",rc)
client = mqtt.Client()
airprs_data=0
dirthump_data=0
sunlight_data=0
temp_data=0
hump_data=0

#mqtt connect to borker
def mqttconnect():
    client.username_pw_set("silence", "silence0802")
    client.on_connect = on_connect
    client.connect("124.223.169.5", 1883, 60)
    print('connect')




#mqtt uplaod function
def mqttupload(airprs_data,dirthump_data,sunlight_data,temp_data,hump_data):

    value=[temp_data,hump_data,dirthump_data,sunlight_data,airprs_data]
    quality=['temp','hump','dirthump','sun','press']
    msglen=5  #massage num

    if msglen==1:
        cmd=quality[i]+'":"'+str(value[i])
    if msglen>1:
        for i in range(msglen):
            if i==0:
                cmd=quality[i]+'":"'+str(value[i])
            if i>0:
                cmd=cmd+'"'+','+"\n"+'"'+quality[i]+'":"'+str(value[i])
    client.publish('test1',payload='{'+"\n"+'"'+cmd+'"'+"\n"+'}', qos=0, retain=False) #mqtt topic publish
    print("send msg to test1")
    


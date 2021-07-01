#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from datetime import datetime
import re
import requests
import paho.mqtt.client as paho

motion_urls = {}
with open("/etc/motioneye/mqtt.txt") as f:
    for line in f:
        (key, val) = line.split()
        motion_urls[key] = val

def on_message_temp(mosq, obj, msg):
    raw=datetime.now()
    now=raw.strftime("%Y-%m-%d %H:%M:%S")
    tempf=re.search(r'\-*\d+\.*\d*', str(msg.payload)).group()
    tempf=round(float(tempf),1)
    for camera_name in motion_urls:
        message=f"{camera_name}%20{tempf}F"
        setcmd= {'text_left': message}
        r=requests.get(motion_urls[camera_name], params=setcmd, timeout=5)
        print ("%s %s" % (now, r.url))


mqttc = paho.Client()
mqttc.message_callback_add('weewx/outTemp_F', on_message_temp)
mqttc.connect("192.168.44.5", 1883, 30)
mqttc.subscribe("weewx/#")

mqttc.loop_forever()


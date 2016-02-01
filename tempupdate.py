#!/usr/bin/python

import time
import requests
from thermos import *

HCL_IP = "192.168.1.15"
HCL_USER = "user"
HCL_PASS = "pass"
LOG_FILE = "/var/log/thermos.log"
HCL_VD_ID = "56"
HCL_VD_TEMP_SLIDER_ID = "1"
TEMP_UPDATE_INTERVAL = 60

class Debug:
	def __init__(self,message):
		self.message = message+"\n"
	def write(self):
		file = open(LOG_FILE,"a")
		timestamp = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(int(time.time())))
		file.write(timestamp)
		file.write(self.message)
		file.close()
class TempUpdate:
	def __init__(self,updateInterval):
		self.uInterval = updateInterval
		self.thermosID = HCL_VD_ID
		self.sliderID = HCL_VD_TEMP_SLIDER_ID
		
	def getUrl(self,url):
		try:
			Debug("-- URL : "+ url ).write()
			return requests.get(url, timeout=1)
		except requests.exceptions.Timeout:
			Debug("-- Timeout for request: " + url ).write()
			return None
	
	def start(self):
		Debug("-- Starting VD temperature update process").write()		
		while True:
		    authorization = ClientAuth()
    		    thermos = Thermos (authorization)
		    url = "http://"+HCL_USER+":"+HCL_PASS+"@"+HCL_IP+"/api/callAction?deviceID=" + self.thermosID + "&name=setSlider&arg1=" + self.sliderID + "&arg2=" + str(int(round(thermos.measTemp)))
		    resp = self.getUrl(url)
		    Debug("-- HCL response status: " + (str(resp.status_code) if(resp is not None) else "None")).write()
		    time.sleep(1)
		    update = 0
		    time.sleep(self.uInterval)

if __name__ == "__main__":
    updater = TempUpdate(TEMP_UPDATE_INTERVAL)
    updater.start()
    
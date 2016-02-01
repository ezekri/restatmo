import json, time
import requests.packages.urllib3
from urllib import urlencode
import urllib2


# User identification data
_CLIENT_ID     		= "xxxxxxxxxxxxx"   #client ID from http://dev.netatmo.com/dev/listapps
_CLIENT_SECRET 		= "xxxxxxxxxxxx"   #client app secret
_USERNAME      		= "xxxxx@xxx.xxx"   #netatmo username
_PASSWORD      		= "xxxxxxxxx"   # netatmo password



# netatmo API
_BASE_URL       	= "https://api.netatmo.net/"
_AUTH_REQ       	= _BASE_URL + "oauth2/token"
_GETTHERMOSTATDATA_REQ	= _BASE_URL + "api/getthermostatsdata"
_SETTEMP_REQ		= _BASE_URL + "api/setthermpoint"


class ClientAuth:
    def __init__(self, clientId=_CLIENT_ID,
                       clientSecret=_CLIENT_SECRET,
                       username=_USERNAME,
                       password=_PASSWORD):

        postParams = {
                "grant_type" : "password",
                "client_id" : clientId,
                "client_secret" : clientSecret,
                "username" : username,
                "password" : password,
                "scope" : "read_thermostat write_thermostat"
                }
        resp = postRequest(_AUTH_REQ, postParams)

        self._clientId = clientId
        self._clientSecret = clientSecret
        self._accessToken = resp['access_token']
        self.refreshToken = resp['refresh_token']
        self._scope = resp['scope']
        self.expiration = int(resp['expire_in'] + time.time())

    @property
    def accessToken(self):

        if self.expiration < time.time(): # Token should be renewed

            postParams = {
                    "grant_type" : "refresh_token",
                    "refresh_token" : self.refreshToken,
                    "client_id" : self._clientId,
                    "client_secret" : self._clientSecret
                    }
            resp = postRequest(_AUTH_REQ, postParams)

            self._accessToken = resp['access_token']
            self.refreshToken = resp['refresh_token']
            self.expiration = int(resp['expire_in'] + time.time())

        return self._accessToken

class Thermos:

    def __init__(self, authData):

        self.accessToken = authData.accessToken
	postParams = {
                "access_token" : self.accessToken
                }
        resp = postRequest(_GETTHERMOSTATDATA_REQ, postParams)
        self.rawData = resp['body']
	self.status = resp['status']
        self.devList = self.rawData['devices']
	self.devId = self.devList[0]['_id']
	self.modList = self.devList[0]['modules']
	self.modId = self.modList[0]['_id']
	self.measTemp = self.modList[0]['measured']['temperature']
	self.setPointTemp = self.modList[0]['measured']['setpoint_temp']
	
	
    def setTemp(self,mode, temp, endTimeOffset ):
        postParams = { "access_token" : self.accessToken }
        postParams['device_id']  = self.devId
        postParams['module_id']  = self.modId
        postParams['setpoint_mode']      = mode
        if mode == "manual":
		postParams['setpoint_endtime']       = time.time() + endTimeOffset
        	postParams['setpoint_temp'] = temp
        return postRequest(_SETTEMP_REQ, postParams)

    @property
    def device_id(self):
        return self.devId

    @property
    def mod_id(self):
        return self.devId

    @property
    def measTemp(self):
        return self.measTemp

    @property
    def setPointTemp(self):
        return self.setPointTemp

    @property
    def status(self):
        return self.status


def postRequest(url, params):
   params = urlencode(params)
   headers = {"Content-Type" : "application/x-www-form-urlencoded;charset=utf-8"}
   req = urllib2.Request(url=url, data=params, headers=headers)
   resp = urllib2.urlopen(req).read()
   return json.loads(resp)
   

if __name__ == "__main__":

    #test it
    from sys import exit, stdout, stderr
    
    if not _CLIENT_ID or not _CLIENT_SECRET or not _USERNAME or not _PASSWORD :
           stderr.write("Library source missing identification arguments")
           exit(1)
    authorization = ClientAuth()
    thermos = Thermos (authorization)
    thermos.setTemp("manual", 20, 120)	
    exit(0)

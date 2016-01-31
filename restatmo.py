#!/usr/bin/python

from thermos import *
from flask import Flask,jsonify
from flask_restful import Resource, Api
import urllib

DEFAULT_DURATION = 15

app = Flask(__name__)
api = Api(app)

class TempSP(Resource):
    def get(self):
	authorization = ClientAuth()
    	thermos = Thermos (authorization)
    	return jsonify({'temperatureSetPoint': str(thermos.setPointTemp)})
    
    def post(self, tempSP):
	authorization = ClientAuth()
    	thermos = Thermos (authorization)
	if tempSP == 0:
		thermos.setTemp("program", None, None)	
	elif tempSP == 101:
		thermos.setTemp("away", None, None)
	else:
		thermos.setTemp("manual", tempSP, DEFAULT_DURATION*60)
    	return jsonify({'temperatureSetPoint': tempSP, 'duration': str(DEFAULT_DURATION*60)})

class TempDur(Resource):
    def post(self, duration):
	authorization = ClientAuth()
    	thermos = Thermos (authorization)
	thermos.setTemp("manual", thermos.setPointTemp, duration*60)
	return jsonify({'temperatureSetPoint': str(thermos.setPointTemp), 'duration': duration*60})

class TempMeas(Resource):
    def get(self):
	authorization = ClientAuth()
    	thermos = Thermos (authorization)
	return jsonify({'measuredTemperature' : str(thermos.measTemp)})
    
      
api.add_resource(TempSP, '/tempSP', endpoint="tempSP")
api.add_resource(TempSP, '/tempSP/<int:tempSP>', endpoint="tempSPVal")
api.add_resource(TempMeas, '/tempMeas', endpoint="tempMeas")
api.add_resource(TempDur, '/tempDur/<int:duration>', endpoint="tempDuration")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
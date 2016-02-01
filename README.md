# restatmo
Simple Restful web service to manage Netatmo Thermostat
Use case : controlling Netatmo thermostat from Fibaro HCL box

# Description 
Control Netatmo thermostat with simple HTTP requests:
GET /tempSP : get current temperature set point 
SET /tempSP/<int:tempSP> : set new temperaure set point
SET /tempDur/<int:duration> : set temperature set point endtime
GET /tempMeas : get measured temperature


# Use Case
This web service can be used by Fibaro HCL in a Virtual Device


# Dependencies
Python flask [library](http://flask.pocoo.org/)

Python flask_restful [library](http://flask-restful-cn.readthedocs.org/en/0.3.4/installation.html#installation) 


# Install
git clone https://github.com/ezekri/restatmo.git

# Configure global variables

in thermos.py file :

_CLIENT_ID : Netatmo Client ID from http://dev.netatmo.com/dev/listapps

_CLIENT_SECRET : Netatmo Client app secret

_USERNAME : Netatmo username

_PASSWORD : Netatmo password

in tempupdate.py :

HCL_IP : Fibaro HCL IP address

HCL_USER : HCL user name

HCL_PASS : HCL password

LOG_FILE : Log file path

HCL_VD_ID : HCL virtual device ID

HCL_VD_TEMP_SLIDER_ID : HCL temperature slider ID

TEMP_UPDATE_INTERVAL : Update interval for HCL virtual device temperature

# Configure startup services

- edit "restatmo" and "tempupdate" files and define the right restatmo path in RESTATMO_PATH variable

From restatmo folder do this:

chmod +x restatmo.py

sudo cp restatmo /etc/init.d/

sudo chmod 755 /etc/init.d/restatmo

sudo update-rc.d restatmo defaults

chmod +x tempupdate.py

sudo cp tempupdate /etc/init.d/

sudo chmod 755 /etc/init.d/tempupdate

sudo update-rc.d tempupdate defaults


# start/stop/status restatmo
sudo service homegw start

sudo service homegw stop

sudo service homegw status

# start/stop/status tempupdate
sudo service tempupdate start

sudo service tempupdate stop

sudo service tempupdate status


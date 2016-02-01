# restatmo
Simple Restful web service to manage Netatmo Thermostat

# Web service description 
Control Netatmo thermostat with simple HTTP requests:

GET /tempSP : get current temperature set point

SET /tempSP/<int:tempSP> : set new temperaure set point

SET /tempDur/<int:duration> : set temperature set point endtime

GET /tempMeas : get measured temperature

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

# Configure startup services

- edit "restatmo" file and define the right restatmo path in RESTATMO_PATH variable

From restatmo folder do this:

chmod +x restatmo.py

sudo cp restatmo /etc/init.d/

sudo chmod 755 /etc/init.d/restatmo

sudo update-rc.d restatmo defaults

# start/stop/status restatmo service
sudo service homegw start

sudo service homegw stop

sudo service homegw status

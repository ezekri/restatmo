# restatmo
Simple Restful web service to manage Netatmo Thermostat

Optional : Deamon to update Netatmo Virtual device temperature in Fibaro Home Center Box

# Web service description 
Control Netatmo thermostat with simple HTTP requests:

GET /tempSP : get current temperature set point

SET /tempSP/<int:tempSP> : set new temperaure set point

SET /tempDur/<int:duration> : set temperature set point endtime

GET /tempMeas : get measured temperature

# Dependencies
Python flask [library](http://flask.pocoo.org/)

Python flask_restful [library](http://flask-restful-cn.readthedocs.org/en/0.3.4/installation.html#installation) 

Tested in Raspberry Pi with Raspbian Wheezy OS. For other Linux distributions, please check how to set up a startup service.

# Install
git clone https://github.com/ezekri/restatmo.git

# Configure global variables

in thermos.py file :

_CLIENT_ID : Netatmo Client ID from http://dev.netatmo.com/dev/listapps

_CLIENT_SECRET : Netatmo Client app secret

_USERNAME : Netatmo username

_PASSWORD : Netatmo password

# Configure startup services

- Edit "restatmo" file and define the right restatmo path in RESTATMO_PATH variable

In restatmo folder do this:

chmod +x restatmo.py

sudo cp restatmo /etc/init.d/

sudo chmod 755 /etc/init.d/restatmo

sudo update-rc.d restatmo defaults

- If you want to update temperature of Fibaro Home Center netatmo virtual device, configure tempupdate service like this

In restatmo folder do this:

chmod +x tempupdate.py

sudo cp tempupdate /etc/init.d/

sudo chmod 755 /etc/init.d/tempupdate

sudo update-rc.d tempupdate defaults

(Don't forget to set up Fibaro Home Center authentication parameters and Virtual Device ID) 

# start/stop/status restatmo service
sudo service restatmo start

sudo service restatmo stop

sudo service restatmo status

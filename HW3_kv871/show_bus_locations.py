{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "#got help from christine and cyrus\n",
    "#martha showed me how to convert to a py file and run that in my terminal\n",
    "\n",
    "\n",
    "import pylab as pl\n",
    "import pandas as pd\n",
    "import os\n",
    "import json\n",
    "import sys\n",
    "try:\n",
    "    import urllib2 as urllib\n",
    "except ImportError:\n",
    "    import urllib.request as urllib\n",
    "    \n",
    "from __future__ import print_function"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Populating the interactive namespace from numpy and matplotlib\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/usr/local/Anaconda3-5.0.0-Linux-x86_64/envs/PUI2016_Python3/lib/python3.5/site-packages/IPython/core/magics/pylab.py:161: UserWarning: pylab import has clobbered these variables: ['var']\n",
      "`%matplotlib` prevents importing * from pylab and numpy\n",
      "  \"\\n`%matplotlib` prevents importing * from pylab and numpy\"\n"
     ]
    }
   ],
   "source": [
    "%pylab inline\n",
    "pl.rc ('font', size=15)\n",
    "this_key= 'f7ec514a-23b0-4fc6-a89e-e9408bee9b6c'\n",
    "this_bus='B44'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['Siri'])\n"
     ]
    }
   ],
   "source": [
    "url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + this_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + this_bus\n",
    "\n",
    "#print (url)\n",
    "response = urllib.urlopen(url)\n",
    "data = response.read().decode(\"utf-8\")\n",
    "data = json.loads(data)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=f7ec514a-23b0-4fc6-a89e-e9408bee9b6c&VehicleMonitoringDetailLevel=calls&LineRef=B44\n"
     ]
    }
   ],
   "source": [
    "url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + this_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + this_bus\n",
    "print (url)\n",
    "response = urllib.urlopen(url)\n",
    "data = response.read().decode(\"utf-8\")\n",
    "data = json.loads(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bus Line: B44\n",
      "Number of Active Busses: 9\n",
      "Bus 0 is at Latitude: 40.663916 and Longitude: -73.948082\n",
      "Bus 1 is at Latitude: 40.709361 and Longitude: -73.95966\n",
      "Bus 2 is at Latitude: 40.61001 and Longitude: -73.943673\n",
      "Bus 3 is at Latitude: 40.706979 and Longitude: -73.961343\n",
      "Bus 4 is at Latitude: 40.709557 and Longitude: -73.960216\n",
      "Bus 5 is at Latitude: 40.610339 and Longitude: -73.943731\n",
      "Bus 6 is at Latitude: 40.648102 and Longitude: -73.949295\n",
      "Bus 7 is at Latitude: 40.584035 and Longitude: -73.936261\n",
      "Bus 8 is at Latitude: 40.679182 and Longitude: -73.949627\n"
     ]
    }
   ],
   "source": [
    "path=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']\n",
    "print ('Bus Line:',this_bus)\n",
    "print ('Number of Active Busses:', len(path))\n",
    "bus_number=0\n",
    "for i in path:\n",
    "    print('Bus',bus_number, 'is at','Latitude:',i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],'and Longitude:',i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])\n",
    "    bus_number+=1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#need to loop through array at the end \n",
    "#columns: latitude, longitude, stop name, stop status \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PUI2016_Python3",
   "language": "python",
   "name": "pui2016_python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

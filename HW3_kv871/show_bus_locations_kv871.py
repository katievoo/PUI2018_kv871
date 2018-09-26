
#got help from christine and cyrus and martha and nathan
#martha showed me how to convert to a py file and run that in my terminal

from __future__ import print_function

import pylab as pl
import pandas as pd
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
   


this_key=str(sys.argv[1])
this_bus=str(sys.argv[2])


url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + this_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + this_bus

#print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

path=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print ('Bus Line:',this_bus)
print ('Number of Active Busses:', len(path))
bus_number=0
for i in path:
    print('Bus',bus_number, 'is at','Latitude:',i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],'and Longitude:',i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    bus_number+=1

#need to loop through array at the end 
#columns: latitude, longitude, stop name, stop status 


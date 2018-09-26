
# coding: utf-8

# In[137]:


#got help from christine and cyrus
#martha showed me how to convert to a py file and run that in my terminal


import pylab as pl
import pandas as pd
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
    
from __future__ import print_function


# In[138]:


get_ipython().run_line_magic('pylab', 'inline')
pl.rc ('font', size=15)
this_key= 'f7ec514a-23b0-4fc6-a89e-e9408bee9b6c'
this_bus='B44'


# In[139]:


url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + this_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + this_bus

#print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

print (data.keys())


# In[140]:


(type(data))


# In[141]:


data.keys()


# In[142]:


url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + this_key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + this_bus
print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)


# In[143]:


data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']


# In[136]:


path=data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
for i in path 
    print ('Bus Line:', i['MonitoredVehicleJourney'][] )
print ('Number of Active Busses:', len(path))
for i in path:
    print(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    print(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])


# In[ ]:


python show_bus_locations.py f7ec514a-23b0-4fc6-a89e-e9408bee9b6c B44


# In[ ]:


#need to loop through array at the end 
#columns: latitude, longitude, stop name, stop status 


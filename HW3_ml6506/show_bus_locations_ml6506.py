#!/usr/bin/env python
from __future__ import print_function
import json
import os
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
 
key=sys.argv[1]
bus_line=sys.argv[2]

print(key)
print(bus_line)

bus_url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+key+"&VehicleMonitoringDetailLevel=calls&LineRef="+bus_line

print("Bus Line:"+bus_line)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")

bus_num = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
bus_num_str = "Number of Active Buses : "
bus_x = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print(bus_num_s, bus_num)
  for i in range(len(bus_x)):
    lat = bus_x[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    long = bus_x[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
     print("Bus "+str(i)+" is at latitude "+str(lat)+" and longitude "+str(long))

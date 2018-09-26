#!/usr/bin/env python
from __future__ import print_function 
import os
import sys
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

key = sys.argv[1]
bus_line = sys.argv[2]
file_name = sys.argv[3]

print(key)
print(bus_line)
print(file_name)

bus_url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+key+"&VehicleMonitoringDetailLevel=calls&LineRef="+bus_line+file_name

print("Bus Line:"+bus_line)

js_file=requests.get(bus_url).json()
buses=js_file['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
num_buses=len(buses)

#create dataframe
columns = ['Latitude','Longitude','Stop Name','Stop Status']
dataframe = pd.DataFrame(columns=columns)
for x in range(num_buses):
    long=buses[x]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    lat=buses[x]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    try:
        stop_nm=buses[x]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stop_sta=buses[x]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
#    if len(buses[x]['MonitoredVehicleJourney']['OnwardCalls'])==0:
    except:
        stop_nm="N/A"
        stop_sta="N/A"
#    else:
    finally:
        for_ap = pd.DataFrame([[lat,long,stop_nm,stop_sta]], columns=['Latitude','Longitude','Stop Name','Stop Status'])
        dataframe=dataframe.append([for_ap])
dataframe.to_csv(filename,header=True, index=False, encoding='utf-8')

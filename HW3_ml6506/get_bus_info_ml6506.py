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

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

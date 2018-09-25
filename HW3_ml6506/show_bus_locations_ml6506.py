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

bus_url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+key+"&VehicleMonitoringDetailLevel=calls&LineRef="+bus_line
print

#quick little IP geolocation script I threw together. Gives your public IP, region of world/country, country, city, and org.
#usage is just 'python ipgeo.py' and you are all set, assuming you have the imported modules.

import re
import json
from urllib2 import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

print 'Your IP detail\n '
print 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP)

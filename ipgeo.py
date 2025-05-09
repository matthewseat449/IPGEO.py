#quick little IP geolocation script I threw together. Gives your public IP, region of world/country, country, city, and org.
#usage is just 'python ipgeo.py' and you are all set, assuming you have the imported modules.

#edited usage for python3 - functions are the exact same,but using python3 instead of 2
import json
from urllib.request import urlopen

def get_ip_info():
    url = 'http://ipinfo.io/json'
    with urlopen(url) as response:
        data = json.load(response)

    ip = data.get('ip', 'N/A')
    org = data.get('org', 'N/A')
    city = data.get('city', 'N/A')
    country = data.get('country', 'N/A')
    region = data.get('region', 'N/A')

    print('Your IP detail\n')
    print('IP      : {}'.format(ip))
    print('Region  : {}'.format(region))
    print('Country : {}'.format(country))
    print('City    : {}'.format(city))
    print('Org     : {}'.format(org))

if __name__ == '__main__':
    get_ip_info()

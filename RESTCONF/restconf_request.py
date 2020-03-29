import requests
import json
from pprint import pprint

router={"ip": "ios-xe-mgmt.cisco.com", "port":"9443", "user":"root", "password":"D_Vay!_10&"}
headers={'Accept':'application/yang-data+json',
         'Content-Type':'application/yang-data+json',
         'Authorization': 'Basic cm9vdDpEX1ZheSFfMTAm'}

url = f"https://{router['ip']}:{router['port']}/restconf/data/ietf-interfaces:interfaces"
#without the f and {}, the router dict will be consideres a string
#and the api calls will fail to parse router['ip']:router['port']

print (url)
response = requests.get(url, headers=headers,
           auth=(router['user'],router['password']), verify=False)
api_pydata = response.json()

##For readability we parse to Json
api_jdata = json.dumps(api_pydata, indent=4, sort_keys=True)

#print (api_pydata)
print (api_jdata)

#print(response.text.encode('utf8'))

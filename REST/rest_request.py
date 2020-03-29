
# ###########TEMPLATE###########
# import request
# url = "http://example.com"
# headers = {}
# payload = {}
# response = requests.request('GET', headers=headers, data=payload)
# py_dict = response.json
# py_text = response.text.unicode(utf8)

import requests
import json
from pprint import pprint

url = "https://postman-echo.com/get"

payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data = payload)
#response needs to be decoded either as a text code, python, JSON, xml)
#1. convert response to python dict - Required to extract items in dict
resp_py = response.json()
#2. convert python dict  to json with idents - Required for reading
resp_js = json.dumps(resp_py,indent=2, sort_keys=True)
print (resp_js)
#3. Alternatively convert response to simple string py_text and prints
print(response.text.encode('utf8')) 
#Parse an item in the json py_text
print (resp_py['headers']['x-forwarded-port'])

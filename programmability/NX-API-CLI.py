import requests
import json

url = "https://sbx-nxos-mgmt.cisco.com/ins"
#Payload is formatted from POSTMAN
payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "sh ip int bri",
    "output_format": "json"
  }
}
headers = {
  'Authorization': 'Basic YWRtaW46QWRtaW5fMTIzNCE=',
  'Content-Type': 'application/json',
  'Cookie': 'nxapi_auth=admin:yQaFEGmWUFdXU4VTvvkhRE7z9+4='
}

response = requests.request("POST", url, headers=headers, data = json.dumps(payload), verify=False)

#print(response.text.encode('utf8'))
resp_py = response.json()
#2. convert python dict  to json with idents - Required for reading
resp_js = json.dumps(resp_py,indent=2, sort_keys=True)
print (resp_js)

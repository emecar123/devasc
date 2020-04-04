import requests
import json

url = "https://sbx-nxos-mgmt.cisco.com/api/aaaLogin.json"

payload = {
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "Admin_1234!"
    }
  }
}

headers = {
  'Content-Type': 'application/json',
  #'Cookie': 'nxapi_auth=admin:yQaFEGmWUFdXU4VTvvkhRE7z9+4=; APIC-cookie=WlxdbRKsKH2pImAP6ot1RX0bK6PVX0BH6e6QYRCmk/FDrrdC28Ews7BYc8wAaBkxI0TKnT/LG2SKbj46eGlS9cBBxdB0YXsuKVQynZE57KxhWkdF6I1UMFlbXRwAP5iRGMUUmibdIQCljfaLiU48Ra7Ea75Jck+Np17/zBymWnc='
}

response = requests.request("POST", url, headers=headers, data = json.dumps(payload), verify=False)

resp_py = response.json()
#2. convert python dict  to json with idents - Required for reading
resp_js = json.dumps(resp_py,indent=2, sort_keys=True)
#print (resp_js)

token = resp_py['imdata'][0]['aaaLogin']['attributes']['token']
#print(token)
########## GET REQUEST FOR INT VLAN 1###########################################
cookies = {}
cookies['APIC-cookie']=token
url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/bd/bd-[vlan-1].json"
payload = {}
headers= {}
response = requests.request("GET", url, headers=headers, data=payload, cookies=cookies, verify=False)
resp_py = response.json()
resp_js = json.dumps(resp_py,indent=2, sort_keys=True)
print(resp_js)

########## PUT REQUEST FOR INT ETH1/1###########################################
cookies = {}
cookies['APIC-cookie']=token
url = "https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/phys-[eth1/1].json"
payload = {
    "l1PhysIf": {
        "attributes": {
            "descr": "Configured with NX-API RESTXX"
        }
    }
}
headers = {
  'Content-Type': 'application/json',
  }
response = requests.request("PUT", url, headers=headers,
 data=json.dumps(payload), cookies=cookies, verify=False)
resp_py = response.json()
resp_js = json.dumps(resp_py,indent=2, sort_keys=True)
print(resp_js)

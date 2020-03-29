from ncclient import manager
import xmltodict
import  xml.dom.minidom
from router_info import router
from pprint import pprint


netconf_filter =  open("netconf_filter.xml").read()

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
        interface_netconf = m.get(netconf_filter)
        ###    #xmlDom #########################################
        xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
        print (xmlDom.toprettyxml(indent=" "))
        print ('*' * 25 + 'Break' + '*' * 50)
        #####  #xmltodict ######################################
        interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]

pprint (interface_python)   #######Fancy Printing#######

#name = interface_python["interfaces"]["interface"]['#text']
config = interface_python["interfaces"]["interface"]
op_state = interface_python["interfaces-state"]["interface"]

print ("name :" + config["name"]["#text"])
print ("Description: " + config["description"])
print ("Packets In: " + op_state["statistics"]["in-unicast-pkts"])

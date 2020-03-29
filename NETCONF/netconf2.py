from ncclient import manager
import xmltodict
import  xml.dom.minidom
from router_info import router


netconf_filter =  open("netconf_filter.xml").read()

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
        interface_netconf = m.get_config("running", netconf_filter)
        xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
        print (xmlDom.toprettyxml(indent=" "))
        print ('*' * 25 + 'Break' + '*' * 50)

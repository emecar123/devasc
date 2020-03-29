from ncclient import manager
import xmltodict
import  xml.dom.minidom
netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces>
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces-state>
</filter>
"""
router = {"host": "10.10.20.48", "port":"830", "username":"cisco", "password":"cisco_1234!"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    with open("IOS-XE-capability2.txt", mode="w") as ext_file:
        for capability in m.server_capabilities:
            ext_file.write ('*' * 50 + '\n')        #Replaces print
            ext_file.write (capability + '\n')      #Replaces print
        interface_netconf = m.get(netconf_filter)
        xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
        print (xmlDom.toprettyxml(indent=" "))
        print ('*' * 25 + 'Break' + '*' * 50)

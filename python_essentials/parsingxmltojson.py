import xmltodict

with open('C:/Users/MR EMEKA/py3-venv/devasc/rawfiles/customer.xml') as xml_file:
    py_file = xmltodict.parse(xml_file.read())

print (py_file)

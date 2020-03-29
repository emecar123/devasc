import json
from pprint import pprint
import os
my_name = {'Name': 'Innocent' , 'Surname': 'Egbunonu'}
#COMPLETE WAY TO LOAD A JSON FILE FROM ANY BASH POINT RUN DIRECTORY
# here = os.path.abspath(os.path.dirname(__file__))
# print (here)
# with open(os.path.join(here, "interface-config.json")) as file:
#      json_text = file.read()  #This is a string
#      #print (type(json_text))
#      py_dict = json.loads(json_text) #This is native python dict
#      print (py_dict)
#      print (type(py_dict))

# # #SMATTER WAY TO SERIALIZE A JSON FILE TO PYTHON
# with open('C:/Users/MR EMEKA/py3-venv/devasc/rawfiles/interface-config.json') as json_file:
#    python_file = json.load(json_file)
# #
#print (python_file)
#
# #DESERIALIZING PYTHON DATA TO JSON
with open('C:/Users/MR EMEKA/py3-venv/devasc/rawfiles/json_file.json', 'w') as f:
     json.dump(my_name, f )

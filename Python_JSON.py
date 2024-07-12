#NOTE: 
'''
JSON serialization (json.dumps()) is used to convert Python data structures into a JSON formatted
string, while JSON deserialization (json.loads()) converts JSON formatted strings back into Python data structures. 
This process is essential for data interchange between different systems or for storing data in a structured format that
is easy to read and parse.
----------------------------------------------------------------------------------------------------------------'''
import json

#Python Dictionary to JSON:----->

person={
    "Name"   : "Ali",
    "ID"     : 456020,
    "Call"   : 901838473849,
    "Address": "NYC"
}
conv1=json.dumps(person, indent=4)
print(conv1)

#Now JSON string to Python:------>

x='{"Name": "Ali", "ID": 456020, "Call": 901838473849, "Address": "NYC"}'
conv2=json.loads(x)
print(conv2)
#--------------------------------------------------------------------------------------

#Now Python list to JSON string :---->

my_list=["car", "banana", "tower", "mango"]
conv3=json.dumps(my_list, indent=4, sort_keys=True)
print(conv3)

#Now JSON string to Python list:------>
json_string='["car", "banana", "tower", "mango"]'
conv4=json.loads(json_string)
print(conv4)
#-------------------------------------------------------

'''
now same thing but using "try except" rule
'''

person_info={
    "Name"   : "Ali",
    "ID"     : 456020,
    "Call"   : 901838473849,
    "Address": "NYC"
}
my_list_info=["car", "banana", "tower", "mango"]

#let's convert:
try:
    conv11= json.dumps(person_info, indent=4)
    try:
        print(conv11)
    except:
        print("Can't print")
except:
    print("Can't convert")
    
try:
    conv12= json.dumps(my_list_info,indent=4, sort_keys=True)
    try:
        print(conv12)
    except:
        print("Can't print")
except:
    print("Can't convert")

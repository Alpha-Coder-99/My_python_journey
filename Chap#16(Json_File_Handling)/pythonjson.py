#Json Stands for Java script Object Notation
#It is mainly used for storing and tranferring data between the browser & server
#Json is text ,written in javascript object Notation
#Python too support Json  with a biult -in package called jason

import json
d={
    "jar1":"salt",
    "jar2":"chilli powder",
    "jar3":"Chaat_masala",
    "Is_salt":True
}
f=json.dumps(d)
print(f)
print(type(f))
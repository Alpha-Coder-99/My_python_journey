"""All Classes have a function i called -init- function
Which is always executed when the object is bieng 
initiated """
"__init__ ka matlab hai 'Initialize'."
"""Ye wo function hai jo tab chalta hai jab aap koi naya Object banate hain.
Jaise hi koi bacha paida hota hai,
 uska naam aur rang pehle se tay hota hai,
 waise hi __init__ object ko uski pehli values (attributes) deta hai."""

class Student:
    name="Raha"
    def __init__(self):
        print("Adding new student in Database...")
        print(self)
    

# print("student")

#Creating Objects/instances of classes
s1=Student()
print(s1.name)
# s2=Student()
# print(s2.name)

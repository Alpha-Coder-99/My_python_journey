"""All Classes have a function i called -init- function
Which is always executed when the object is bieng 
initiated """
"__init__ ka matlab hai 'Initialize'."
"""Ye wo function hai jo tab chalta hai jab aap koi naya Object banate hain.
Jaise hi koi bacha paida hota hai,
 uska naam aur rang pehle se tay hota hai,
 waise hi __init__ object ko uski pehli values (attributes) deta hai."""

# class Student:
#     name="Raha"
#     def __init__(self):
#         print("Adding new student in Database...")
#         print(self)
    

# # print("student")

# # Creating Objects/instances of classes
# s1=Student()
# print(s1.name)
# # s2=Student()
# # print(s2.name)




class Student:

    def __init__(self,fullname,marks):
        self.fullname=fullname
        self.marks=marks
        print("adding new student in  data base...  ")

s1=Student("Mariyam",56)
print(s1.fullname,s1.marks)
s2=Student("Batool",78)
print(s2.fullname,s2.marks)
s3=Student("Sara",45)
print(s3.fullname,s3.marks)
        
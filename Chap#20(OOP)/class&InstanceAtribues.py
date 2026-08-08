class Student:
    school="Inspire"#class attributes
    name="Kiran"
    def __init__(self,fullname,marks):
        self.fullname=fullname #object attributes
        self.marks=marks
        print("adding new student in  data base...  ")

s1=Student("Mariyam",56)
print(s1.fullname,s1.marks,Student.school)
s2=Student("Batool",78)
print(s2.fullname,s2.marks,Student.school)
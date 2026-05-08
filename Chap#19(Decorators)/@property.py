class Student:
    def __init__(self,phy,math,com):
        self.phy=phy
        self.com=com
        self.math=math

    @property
    def percentage(self):
        return str((self.phy+self.com+self.math)/3)+"%"

stu1=Student(81,98,78)
print(stu1.percentage)

stu1.phy=88
print(stu1.percentage)

        
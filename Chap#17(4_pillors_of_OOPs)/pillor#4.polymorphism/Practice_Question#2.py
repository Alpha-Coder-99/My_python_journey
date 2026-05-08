# Define a Employee class with atribites role,department and salary .Thi class also a showDetails() method and
#Create an Engineer class that inherite properties from Employee & has additional atributes :name&age
class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetails(self):
        print(f"role={self.role}")
        print(f"department={self.department}")
        print(f"salary={self.salary}")

e1=Employee("accountant","Finance","80,000")
e1.showDetails()
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","200.000")
    def showDetails(self):
        print(f"name={self.name}")
        print(f"age={self.age}")

eng2=Engineer("Alpha_coder_99","17yearsold")
eng2.showDetails()
        
# Question#1.Define a circle with rdaius r using the constructor
#Define an Area ()method of the class which calculates the area of circle
#Define a parameter() method of the class which allows you to calculate the perimeter of circle
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (22/7)*self.radius**2
    def perameter(self):
        return 2*(22/7)*self.radius
    
c1=Circle(21)
print(c1.area())
print(c1.perameter())
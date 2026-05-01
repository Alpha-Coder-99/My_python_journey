class Car:
    colour="Black"
    @staticmethod
    def start():
        print("Car is starting...")
    @staticmethod
    def stop():
        print("Car is stoping...")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Fortunior")
car2=ToyotaCar("prius")
# print(car1.name)
# print(car2.name)
print(car1.start())
print(car1.colour)
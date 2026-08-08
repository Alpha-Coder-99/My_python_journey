class Car:
    @staticmethod
    def start():
        print("Car is starting...")
    @staticmethod
    def stop():
        print("Car is stoping...")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fortuner("disel")
car1.start()
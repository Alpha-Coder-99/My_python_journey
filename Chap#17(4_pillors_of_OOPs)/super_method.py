class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car is Starting ...")

    @staticmethod
    def stop():
        print("Car is stoping...")

class ToyotaCar(Car):
    def __init__(self, name,type):
        super().__init__(type)
        self.name=name 
        super().start()
car1=ToyotaCar("pirus","Electric")
print(car1.type)
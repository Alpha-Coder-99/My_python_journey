class Car:
    def __init__(self):
        self.acc=False
        self.clutch=False
        self.brk=False
    def start(self):
        self.acc=True
        self.clutch=True
        self.brk=True
        print("Car Started...")

Car1=Car()
Car1.start()



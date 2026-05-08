"""
Object must have the minimum necessary attributes/methods to consider them of certain type, if it looks like a duck and quack like
a duck,It must be a duck
The class or the type of the object is given lesser important in comparision to the methods/attributes
"""
class Vechile:
    run=True

class Car(Vechile):
    def makeSound(self):
        print("Gheeen")

class Bike(Vechile):
    def makeSound(self):
        print("Ghaaan")

Vechiles=[Car(),Bike()]
for vechile in Vechiles:
    vechile.makeSound()

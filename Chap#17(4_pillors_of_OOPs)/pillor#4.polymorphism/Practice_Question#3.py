#Question#3.Create a class called Order which stores item &its price
#Use dunder function __gt__ to convey that:
#order1>order2 if price of order1>price of order2
class Order:
    def __init__ (self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,odr2):
        return self.price >odr2.price
odr1=Order("Juice","100")
odr2=Order("Biscket","50")
print(odr1 < odr2)
print(odr1 > odr2)
class Bikeshop:
    def __init__(self,stock):
        self.stock=stock
    def DisplayBike(self):
        print("Total Bikes",self.stock)
    def RentForBike(self,q):
        if q<=0:
            print("Enter the positive value r greator than zero")
        elif q>self.stock:
            print("Enter the value (less than stock)")
        else:
            self.stock=self.stock-q
            print("total prices:" ,q*100)
            print("Total Bikes",self.stock)

while True:
    obj=Bikeshop(100)
    uc=int(input('''
1.Display Stock
2.Rent a bike
3.Exit
           
           '''))
    if uc==1:
        obj.DisplayBike()
    elif uc==2:
        n=int(input("Enter the quantity:---"))
        obj.RentForBike(n)
    else:
        break

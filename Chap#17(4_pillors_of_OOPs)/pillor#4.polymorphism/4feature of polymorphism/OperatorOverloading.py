"""
Python asli "Method Overloading" ko direct support nahi karta 
(jaisa Java ya C++ mein hota hai). Agar aap ek hi naam ke do functions banayengi, 
toh Python hamesha peeche wale (last one) ko yaad rakhta hai aur pehle wale ko bhool jata hai.
Method Overloading ka matlab hai: "Ek hi kaam, lekin different inputs ke sath."
"""
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i + ",self.img,"j")
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)
    def __mul__(self,num2):
        newReal=self.real*num2.real
        newImg=self.img*num2.img
        return Complex(newReal,newImg)
    def __truediv__(self,num2):
        newReal=self.real/num2.real
        newImg=self.img/num2.img
        return Complex(newReal,newImg)

        
num1=Complex(1,3)
num1.showNumber()
num2=Complex(5,3)
num2.showNumber()
num3=num1+num2
num3.showNumber()
num4=num1-num2
num4.showNumber()
num5=num1*num2
num5.showNumber()
num6=num1/num2
num6.showNumber()
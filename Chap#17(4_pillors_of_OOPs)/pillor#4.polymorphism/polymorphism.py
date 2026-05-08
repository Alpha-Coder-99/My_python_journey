#poly mean many
#morph means forms
#When the same operator is allowed to have diffrent meaning according to the context 
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def showNumber(self):
#         print(self.real,"i + ",self.img,"j")
        
# num1=Complex(1,3)
# num1.showNumber()
# num2=Complex(5,3)
# num2.showNumber()
# oper dia gaya code ko aghr hum us ma dono num 1 +num 2 esa kar ga

# Opertator overloading
#We use dunder ()for this purpose
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
num7=num1+num2
num7.showNumber()
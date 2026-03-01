# Print your name 100 times by uing while loop (While)
num=1
while num <=100:
    print("Alpha_Coder_99")
    num+=1
print("Now loop is ended")  
#WAP to print numbers from 1 to 10 by using while loop
num=1
while num<=10:
    print(num)
    num+=1
print("Question1 complete")
#WAP to print 1o to 1 by using loop 
num=10
while num>=1:
    print(num)
    num-=1
print("Question#2 complete")
# WAP to print all even numbers b/w 1 to 50 by using a while loop
num=2
while num<=50:
    print(num)
    num+=2
# WAP to print all even numbers b/w 1 to 50 by using a while loop by using%
num=1
while num<=50:
    if num%2==0:
        print(num)
        num+=2
# WAP to print all odd numbers b/w 1 to 50 by using a while loop by using%
num=1
while num<=50:
    if num%2!=0:
        print(num)
        num+=2
#Write a program that prints the sum of first n natural numbers e.g,if n=5 then output dhould be :
#1+2+3+4+5=15(Hint:Keep a running tool iside loop)
n=int(input("Enter number:"))  
sum_val=0 
while n>=1:
    sum_val+=n
    n-=1
print("sum:",sum_val)
print("n",n)
#Write a program to print this patern using loop
#*
# **
# ***
# ****
n=1
while n<=4:
    print("*" * n )
    n+=1

#Alpha want to print her name 5 times each time wih a number front of it ,write a program by while loop
n=1
name="Alpha_Coder_99"
while n<=5:
    print(n,name)
    n+=1
#WAP to print the multiplication table of any number using a while loop
num=int(input("Enter anumber:"))
i=1
while i<=10:
    print(f"{num}*{i}=",(num*i))
    i+=1
#WAP to printnumbers 10 to 15 by using while loop
num=10
while num<=15:
    print(num)
    num+=1
#WAP to print the cubes of numbers from 1 to 5 
num=1 
while num <=5:
    print(num ** 3)
    num+=1
# write a program that calculate the product of 1 to 5
num=1
product=1
while num<=5:
    product*=num
    num+=1
print(product)
# Write a program to calculate 3 to the power of 4
base=3
exponent=4
power=print(3**4)
# Write a program to check if a given number is a perfect square
num = int(input("Enter a number to check = "))
i = 1
is_perfect_square = False

while i * i <= num:
    if i * i == num:
        is_perfect_square = True
        break
    i += 1  

if is_perfect_square:
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not perfect square")

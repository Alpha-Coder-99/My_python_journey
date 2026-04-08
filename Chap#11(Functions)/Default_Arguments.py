#If no arguments is provided a default value i used.
def avarege(a=3,b=10):
    avarege_value=(a+b)/2
    print(avarege_value)

# function calling with parameters
avarege(8,4)
avarege(3,9)
avarege(3,2)
avarege(3,42)
avarege()
avarege(5)
avarege(9)




# Write a function that show_age(name,age) that prints"Alpha_Coder is 17 year old" gave default value 
def show_age(name="Alpha_Coder_99",age=17) :
    print(f"{name} is {age} year old")

show_age("Alpha_Warrior",16)
show_age()
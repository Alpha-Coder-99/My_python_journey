# THe return statment use to send a value back from a function
#After return , function stop execution
def multiply(a=5,b=10):
    return a*b

print(multiply(5,9))
result=multiply(3,5)
print(result) 

# Return value ko function ke bahar bhejta hai.
def square(x):
    return x * x
result = square(5)
print(result)
# Difference: - print() → sirf display - return → value store hoti hai

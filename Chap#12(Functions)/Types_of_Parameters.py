# Types of Parameters (Deep Understanding)
# 1. Positional Arguments
# Order matters!
def info(name, age):
    print(name, age)
info("Areeba", 18)
# 2. Keyword Arguments
# Order does NOT matter
info(age=18, name="Areeba")
# 3. Default Parameters
def greet(name="Guest"):
    print("Hello", name)
greet() # Guest
# 4. *args (Multiple Values)
def total(*numbers):
    print(numbers) # tuple
    return sum(numbers)
# 5. **kwargs (Dictionary input)
def details(**data):
    print(data)


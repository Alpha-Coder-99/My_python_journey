def outer():
    def inner():
        return"Hello from inner function"
    print("hello from outer functoion")
    return inner
result=outer()
print(result())
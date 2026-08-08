# The next() function is a built-in Python function used to retrieve the next item from an iterator (like a generator).
#  When next() is called, it tells the generator function to resume execution from its last yield point,
#  run until it hits the next yield, and then pause again.



def count_up_to (n) :
    i=1
    while i<=n:
        yield i
        i+=1


numbers= count_up_to(10)
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))

# Agar aap sirf dir() likhein gi, toh Python batayega ke 
# aap ke apne program mein kitne variables aur functions ban chuke hain.
x=10
name="Areeba"
print(dir())

# import math
# print(dir(math)) # Is mein 'pi', 'sqrt', 'sin', 'cos' sab nazar aayenge

# word="hello"
# print(dir(word))

import my_package.my_module as test_module
print("File location", test_module.__file__)
print("Contents of file:", dir(test_module))
#dir()

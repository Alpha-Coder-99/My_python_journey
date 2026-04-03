#Variables scopes
#Local Variable
"A variable defined inside of the function can be used only within that function "
# for example
def hello():
    message="Hello world🥰"
    print(message)

hello()

#print(message)# if we try to print ., error will occur.NameError: name 'message' is not defined, becoz This is local variable

#Global Variable
"A variable defined outside of the function or in global scope.Global variables can be accessed inside or outside of the function "
message2="Hello world🥰"
def hello2():
    print(message2)

hello2()
print(message2)
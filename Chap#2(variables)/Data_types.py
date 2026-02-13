# 1.Text type(str)
str="The colection of words and chracters writen in double/single quotation is known as string"
print(str)
#2.Numeric Type (int,float,complex)
int=5
float=5.8
complex=2+5j
print(float)
print(int)
print(complex)
#3.Sequence Type(list,tuple,range,and also a str)
list=["apple","Mango","ornge","banana"]#mutable
print(list)
tuple=("apple","banana","cheery")#immutable
print(tuple)
print(range(5))
#4.Mapping type(dict"The collection of keys and pairs is known as dict)
dict={
    "name":"Alpha-coder",
    "age":17,
    "hobby":"cooking&coding"
}
print(dict)
#5.Set type(set""mutble",frozen set'imutable")
set={"apple","mango","cheery"}
print(set)
set_fruits=frozenset(["mango","orange","guava"])
set_fruits.add("strawberry")
print(set_fruits)# ya code error de ga
#6.boolean type(it use for logical operators)
a=True
b=False
print(a)
#7.Binary types(bytes,bytearray,memoryview)
#8None type(kuch bhi nahi jab confirm na ho ka kia value dena hn)
result=None
print(result)
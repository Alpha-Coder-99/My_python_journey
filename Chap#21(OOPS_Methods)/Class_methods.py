# class person :
#     name="anonymous"

#     def ChangeName(self,name):
#         self.__class__.name="Batool"
# p1=person()
# p1.ChangeName("Batool")
# print(p1.name)
# print(person.name)
#IN methods way
class person :
    name="anonymous"
    @classmethod
    def ChangeName(cls,name):
        cls.name=name
    
p1=person()
p1.ChangeName("Batool")
print(p1.name)
print(person.name)

# read only --> you can not set the value. value can not be changed
# gatter --> get a value of a property through a method. most of the time you get the value of a private attribute
# setter --> set a value of a property through a method. Most of the time you will set the value of a private property

class user:
    def __init__(self,name,age,money) -> None:
        self._name = name
        self._age = age
        self.__money = money
        pass
    # gatter
    @property
    def age(self):
        return self._age
    
    def salary(self):
        return self.__money
    
    #setter
    @salary.setter
    def salary(self,value):
        self.__money = value

samsu = user('Kopa' ,21, 12000)

# print(samsu.__money)
# print(samsu.age())
print(samsu.age)

samsu.salary = 4500
print(samsu.salary)
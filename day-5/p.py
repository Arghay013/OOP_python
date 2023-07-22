class student:
    def __init__(self, n, age, salary):
        self.name = n
        self._age = age
        self.__salary = salary
    
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,value):
        self.__salary = value+200
    
S = student('ADP', 21, 4200)
# print(S.__salary)
# print(S.salary)
S.salary = 2300
print(S.salary)

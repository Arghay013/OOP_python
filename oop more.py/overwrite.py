class Person:
    def __init__(self, name,age,height,weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat poolau')
    def exercise(self):
        raise NotImplementedError

class Crickter(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

# over rite
    def eat(self):
        print('vegitable')

    def exercise(self):
        print('gym e poise die gham jhoray')

    def __add__(self, other):
        return self.age + other.age
    def __mul__(self, other):
        return self.weight * other.weight
    

sakib = Crickter('Sakib', 38,68,91,'BD')
musi = Crickter('musi', 38,65,78,'BD')
# sakib.eat()
# sakib.exercise()

#plus overload
print(45+34)
print('sakib' + ' rakib')
print([2,4] + [3, 5])
# print(sakib + musi)
print(sakib * musi)


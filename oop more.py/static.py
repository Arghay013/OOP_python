# static attribute (class attribute)
# static method @staticmethod


class Shopping:
    cart = [] #class stribute / static attribute
    origin = 'chaina'
    def __init__(self,name,location) -> None:
        self.name = 'jamuna city' #instance attribute
        self.location = 'jam er majhe khane'
        pass

    def perchase(self, item, price, amount):
        ramaining = amount - price
        print(f'buying :{item} remaining: {ramaining}')
    @classmethod  
    def hudai_dekhi(self,item):
        print('hudai jaia ac er batash khai')
    @staticmethod
    def mul(a,b):
        print(a*b)

Shopping.perchase('a',2,3,5)
basundhara = Shopping('basundhara','jam er majhe')
basundhara.hudai_dekhi('lungi')
Shopping.hudai_dekhi('lungi')
Shopping.mul(4,5)

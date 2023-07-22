#base class, parent clas, common functionality+attribute
# derived class, child class, uncommon attribute+functionality


class Gadged:
    def __init__(self, brand, price, color, origin) -> None:
        self.brand = brand
        self.color = color
        self.preice = price
        self.color = color
        self.origin = origin
        pass

    def run(self):
        pass



class Laptop:
    def __init__(self, ssd,memory) -> None:
        self.ssd = ssd
        self.memory = memory
        pass
    def run(self):
        return f'Running laptop: {self.brand}'
    def coding(self):
        return f'learning python'
    
class Phone(Gadged):
    def __init__(self, dual_sim,brand, price, color, origin) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, price, color, origin)
        pass


    def phone_call(self, number, text):
        return f'sending message: {self.number}'
    
    def __repr__(self) -> str:
        return f'phone: {self.dual_sim},{self.brand}'


class Camera:
    def __init__(self, pixel) -> None:
        
        self.pixel = pixel

        def change_lens(slef):
            pass
        pass

#inharitense
my_phone = Phone('iphone',120000,'silver','dubai',True)
# my_phone.phone_call()
print(my_phone.brand)
print(my_phone)
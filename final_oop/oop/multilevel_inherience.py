class Vehicle:
    def __init__(self,name, price) -> None:
        self.name = name
        self.price = price
    def move(self):
        pass

class Bus(Vehicle):
    def __init__(self, name, price,seat) -> None:
        self.seat = seat
        super().__init__(name, price)

class Truck(Vehicle):
    def __init__(self, name, price,Weight) -> None:
        self.weight = Weight
        super().__init__(name, price)
# ....>>>>
class Pic_up(Truck):
    def __init__(self, name, price, Weight) -> None:
        super().__init__(name, price, Weight)



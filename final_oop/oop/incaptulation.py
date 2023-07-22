class Bank:
    def __init__(self, holder_name, initial_deposite) -> None:
        self.holder_name = holder_name
        self.__balance = initial_deposite
        pass

    def deposite(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance



rafsan = Bank('Choto bro', 1000)

print(rafsan.holder_name)
# rafsan.balance = 0
# print(rafsan.__balance)
print(rafsan.get_balance())
print(rafsan._Bank__balance)#----->>>>


#        encaptulation ---> hide somethings


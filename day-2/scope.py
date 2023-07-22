balance = 3000
def buy_things(items, price):
    global balance
    """ 
    #if you want to use global variable, you can
    #but if you want to modify it you have to use global keywards"""
    balance = balance - price
    print(f'balance after buying {items}',balance)


buy_things('sunglass',1000)
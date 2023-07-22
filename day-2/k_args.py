""" def full_name(first,last):
    name = f'{first} {last}'
    return name
name = full_name('Alu','kodu')
print (name) """

""" def famous_name(first,last,title,additional):
    name = f'{first} {last} {title} {additional}'
    return name """
# ** kargs -> key wala arguments
""" def famous_name(first,last,**additional):
    name = f'{first} {last}'
    # print(additional['title'])
    for key,value in additional.items():
        print(key,value)
    return name
name = famous_name(first = 'Taher', last = 'Ali', title = 'Hujur',additional = 'molla',last2 = 'taheri') """
# print (name)

def a_lot(num1,num2):
    sum = num1 + num2
    multiple = num1*num2
    remain = num1-num2
    # list
    # return [sum,multiple,remain]
    # touple
    return sum, multiple,remain
print(a_lot(12,5))

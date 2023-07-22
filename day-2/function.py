# define
def double_it(num):
    result = num = num*2
    print(result, end = " ")
    # return result
double_it(8)
double_it(88)

def sum(num1, num2):
    result = num1+num2
    return result
total = sum(44,34)
print('Total is',total)
final = double_it(total)
print('Final value is', final)
import math

def timer(func):
    def inner(*args):
        print('time sterted')
        # print(func)
        func(*args)

        print('time ended')
    return inner

@timer
def get_factorial(n):
    print('factorial starting')
    result = math.factorial(n)
    print(result)

# timer(get_factorial)()

get_factorial(5)


# get_factorial()
# timer()()
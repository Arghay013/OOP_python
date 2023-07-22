# function is a fast class object
def double_dacker():
    print('starting the double decker')
    def inner_func():
        print('inside the inner')
    return inner_func

print(double_dacker())
print(double_dacker()())

def do_something(work):
    print('working')
    # print(work)
    work()
    print('work ended')

def coding():
    print('coding in python')

# do_something(coding)
def sleeping():
    print('sleeping and dreeming')

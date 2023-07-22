# set : unique items collection
numbers = [12 , 56 , 98 , 78, 56 , 12 , 6 , 98]
print(numbers)
num_set = set(numbers)
print(num_set)
num_set.add(55)
print(num_set)
num_set.remove(6)

for item in num_set:
    print(item)

A = {1,3,5}
b = {1,2,3,4,5}
print(A & b)
print(A | b)
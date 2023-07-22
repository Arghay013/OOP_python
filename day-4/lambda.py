# def double(x):
#     return x*2

doubled = lambda num : num*2
squared  = lambda num : num*num

result = doubled(44)
print(result)

add = lambda x,y : x+y
sum = add(11,33)
print(sum)

numbers = [12 , 56 , 98 , 78, 56 , 12 , 6 , 98]

doubled_nums = map(lambda x : x*2,numbers)
print(list(doubled_nums))

actors = [
    {'name': 'sabana', 'age': 18},
    {"name": 'sabnur', 'age': 56},
    {"name": 'sabab', 'age': 78},
    {"name": 'ahad', 'age': 22}
]

juniors = filter(lambda actor : actor['age'] < 40 , actors)
threes = filter(lambda actor : actor['age']%3==0,actors)
# print(list(juniors))
print(list(threes))
x,y = map(int, input().split())
mul = x**0 - 1
pow = 2
while pow<=y:
    mul += x**pow
    pow+=2
print(mul)
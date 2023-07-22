t = int(input())
while t>0:
    x = input()
    y = reversed(x)
    print(*y,sep = ' ')
    t-=1

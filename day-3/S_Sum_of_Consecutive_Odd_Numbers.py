t = int(input())
while t>0:
    a,b = map(int, input().split())
    ans = 0
    x = min(a,b)
    y = max(a,b)
    # print(x,y,end = ' ')
    for i in range (x+1,y):
        if(i%2 == 1):
            ans+=i 
    print(ans)
    t-=1
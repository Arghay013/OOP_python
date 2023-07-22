dp= {}
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n in dp:
        return dp[n]
    dp[n] = fib(n-1)+fib(n-2)
    return dp[n]
x = int(input())
for i in range(1,x+1):
    print(fib(i),end = ' ')
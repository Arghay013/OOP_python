n = int(input())
arr = list(map(int, input().split()))

ans = 0

while True:
    even = True
    for i in range(n):
        if arr[i] % 2 != 0:
            even = False
            break
    
    if not even:
        break

    ans += 1
    for i in range(n):
        arr[i] //= 2

print(ans)

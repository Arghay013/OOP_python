n = int(input())
s = list(map(int, input().split()))
r = 0
ad = {}
for a in s:
    if a in ad:
        ad[a] += 1
    else:
        ad[a] = 1
for key, v in ad.items():
    if v > key:
        r += v-key
    elif v < key:
        r += v
print(r)

K,S = map(int, input().split())
count = 0
for i in range(0,K+1):
    for j in range(0,K+1):
        if S-j-i >= 0 and S-j-i <= K:
            count+=1
        
    
print(count)
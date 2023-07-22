def solve(S):
    count = 0
    ans = []
    temp = ""

    for char in S:
        temp += char
        if char == 'R':
            count += 1
        else:
            count -= 1

        if count == 0:
            ans.append(temp)
            temp = ""

    return ans


S = input()
strings = solve(S)
print(len(strings))
for s in strings:
    print(s)

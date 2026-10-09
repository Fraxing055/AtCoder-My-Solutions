N = int(input())
S = input()

val = 0
ans = 0

for char in S:
    if char == 'I':
        val += 1
    else:
        val -= 1
    ans = max(ans, val)

print(ans)

S = input()
N = len(S)

left = [0] * (N + 1)
right = [0] * (N + 1)

for i in range(N):
    if S[i] == '<':
        left[i + 1] = left[i] + 1

for i in range(N - 1, -1, -1):
    if S[i] == '>':
        right[i] = right[i + 1] + 1

ans = 0
for i in range(N + 1):
    ans += max(left[i], right[i])

print(ans)

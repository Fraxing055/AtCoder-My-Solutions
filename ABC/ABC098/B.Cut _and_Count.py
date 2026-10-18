N = int(input())
S = input()
ans = 0

for i in range(1, N):
  left = set(S[:i])
  right = set(S[i:])
  common = left & right
  ans = max(ans, len(common))
print(ans)

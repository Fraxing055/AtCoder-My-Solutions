S = input()
N = len(S)

ans = 0
for i in range(N):
  if S[i] == 'C':
    ans += min(i+1, N-i)
print(ans)

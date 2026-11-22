N, M = map(int, input().split())
C = []
for _ in range(N):
  C.append(list(map(int, input().split())))

dp = C[0]
for i in range(1, N):
  for h in range(1, M):
    dp[h] = min(dp[h], dp[h - 1])
  for h in range(M):
    dp[h] += C[i][h]
print(min(dp))

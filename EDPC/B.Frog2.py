import sys

N, K = map(int, input().split())
h = list(map(int, sys.stdin.readline().split()))

dp = [10**18] * N
dp[0] = 0

for i in range(1, N):
  for j in range(1, K+1):
    if i - j < 0:
      break
    cand = dp[i-j] + abs(h[i] - h[i-j])
    dp[i] = min(dp[i], cand)

print(dp[-1])

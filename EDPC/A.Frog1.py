import sys

N = int(input())
h = list(map(int, sys.stdin.readline().split()))

dp = [0] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
  cand1 = dp[i-2] + abs(h[i] - h[i-2])
  cand2 = dp[i-1] + abs(h[i] - h[i-1])
  dp[i] = min(cand1, cand2)

print(dp[-1])

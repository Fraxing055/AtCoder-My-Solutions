H, W = map(int, input().split())
G = []
for _ in range(H):
  gd = list(input())
  G.append(gd)
dp = [[0] * W for _ in range(H)]

for i in range(H):
  for j in range(W):
    if i == 0 and j == 0:
      if G[0][0] == '#':
        dp[0][0] = 1
      else:
        dp[0][0] = 0
    elif i == 0:
      if G[i][j] == '#' and G[i][j-1] == '.':
        dp[i][j] = dp[i][j-1] + 1
      else:
        dp[i][j] = dp[i][j-1]
    elif j == 0:
      if G[i][j] == '#' and G[i-1][j] == '.':
        dp[i][j] = dp[i-1][j] + 1
      else:
        dp[i][j] = dp[i-1][j]
    else:
      cand1 = dp[i-1][j]
      if G[i][j] == '#' and G[i-1][j] == '.':
        cand1 += 1
      cand2 = dp[i][j-1]
      if G[i][j] == '#' and G[i][j-1] == '.':
        cand2 += 1
      dp[i][j] = min(cand1, cand2)
      
print(dp[-1][-1])

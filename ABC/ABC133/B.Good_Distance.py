N, D = map(int, input().split())

P = []

for _ in range(N):
  p = list(map(int, input().split()))
  P.append(p)
ans = 0

for i in range(N):
  for j in range(i+1, N):
    cal = 0
    for k in range(D):
      cal += (P[i][k] - P[j][k]) ** 2
    cal = cal ** 0.5
    if cal % 1 == 0:
      ans += 1

print(ans)

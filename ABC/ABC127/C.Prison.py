N, M = map(int, input().split())

lower = 0
upper = 10 ** 5 + 1
for _ in range(M):
  L, R = map(int, input().split())
  lower = max(L, lower)
  upper = min(R, upper)

if lower <= upper:
  print(upper - lower + 1)
else:
  print(0)

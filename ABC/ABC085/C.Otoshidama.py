N, Y = map(int, input().split())
ans = [0, 0, 0]
F = False

for i in range(N+1):
  if 10000 * i > Y:
    ans = [-1, -1, -1]
    break
  for j in range(N - i + 1):
    if 10000 * i + 5000 * j + 1000 * (N - i - j) == Y and min(i, j, N - i - j) >= 0:
      ans = [i, j, N - i - j]
      F = True
      break
  if F == True:
    break
else:
  ans = [-1, -1, -1]
print(f"{ans[0]} {ans[1]} {ans[2]}")

N, M = map(int, input().split())
A = []
for _ in range(N):
  A.append(list(map(int, input().split())))
A.sort()

ans = 0
for i in range(N):
  cal = M - A[i][1]
  if cal >= 0:
    ans += A[i][1] * A[i][0]
  else:
    ans += M * A[i][0]
  if cal <= 0:
    break
  M = cal
print(ans)

N, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for i in range(N):
  x = x - A[i]
  if x < 0:
    print(i)
    break
  elif x == 0:
    print(i + 1)
    break
else:
  if x > 0:
    print(N - 1)
  else:
    print(N)

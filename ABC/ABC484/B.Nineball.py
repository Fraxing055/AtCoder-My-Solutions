K = int(input())
A = list(map(int, input().split()))

if not 9 in A:
  print(-1)
else:
  print(min(A))

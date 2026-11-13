N = int(input())
A = list(map(int, input().split()))

A1 = A[0]
A.remove(A1)

if N == 1:
  print(0)
else:
  K = max(A)
  if A1 > K:
    print(0)
  else:
    print(K - A1 + 1)

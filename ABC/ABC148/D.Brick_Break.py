N = int(input())
A = list(map(int, input().split()))

if not 1 in A:
  print(-1)
else:
  num = 0
  for i in range(len(A)):
    if num + 1 == A[i]:
      num += 1
  print(len(A) - num)

from collections import Counter

N, M = map(int, input().split())

D = {}

for _ in range(N):
  A = list(map(int, input().split()))
  for i in range(M):
    if A[i] in D:
      D[A[i]] += 1
    else:
      D[A[i]] = 1

print(N*M - max(D.values()))

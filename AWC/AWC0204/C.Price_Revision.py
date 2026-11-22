from collections import Counter

N = int(input())
A = list(map(int, input().split()))
S = sum(A)
D = Counter(A)

Q = int(input())

for i in range(Q):
  B, C = map(int, input().split())
  cal = 0
  if B in D:
    cal = (C - B) * D[B]
    D[C] += D[B]
    D[B] = 0
  S += cal
  print(S)

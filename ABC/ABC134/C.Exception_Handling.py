N = int(input())

A = []

for _ in range(N):
  A.append(int(input()))

B = A.copy()
B.sort()

if B[N-1] == B[N-2]:
  for _ in range(N):
    print(B[N-1])
else:
  for i in range(N):
    if A[i] != B[N-1]:
      print(B[N-1])
    else:
      print(B[N-2])

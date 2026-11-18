N, K = map(int, input().split())
L = []
A = []
for _ in range(N):
  I = list(map(int, input().split()))
  L.append(I[0])
  A.append(I[1:])
C = list(map(int, input().split()))

for i in range(len(C)):
  if 0 >= K - L[i] * C[i]:
    digit = K % L[i] - 1
    print(A[i][digit])
    break
  K -= L[i] * C[i]

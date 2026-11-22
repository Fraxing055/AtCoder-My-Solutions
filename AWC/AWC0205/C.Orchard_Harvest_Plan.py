N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
for i in range(N):
  S.append(S[-1] + A[i])

for j in range(Q):
  L, R, T = map(int, input().split())
  print((S[R] - S[L-1]) * T)

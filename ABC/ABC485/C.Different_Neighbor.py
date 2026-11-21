N = int(input())
C = list(map(int, input().split()))
C.append(0)

L = []
R = []
X = 4 * 10 ** 5

F = True
Counter = 0
for i in range(N-1):
  if C[i] == C[i+1]:
    if F == True:
      L.append(X)
    else:
      Counter += 1
      L.append(Counter)
  else:
    F = False
    L.append(1)
    Counter = 0
L.append(L[-1]+1)

Counter = 0
F = True
for j in range(N-1, 0, -1):
  if C[j] == C[j-1]:
    if F == True:
      R.append(X)
    else:
      Counter += 1
      R.append(Counter)
  else:
    F = False
    R.append(1)
    Counter = 0
R.append(R[-1]+1)

ans = []
for k in range(N):
  ans.append(min(L[k], R[N-k-1]))
print(*ans)

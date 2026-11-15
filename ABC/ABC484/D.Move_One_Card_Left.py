from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

ans = 1 + N * (N - 1) // 2

D = defaultdict(int)
D[A[0]] += 1

for i in range(1, N):
  if A[i-1] == A[i]:
    ans -= i
  else:
    ans -= D[A[i]]
  D[A[i]] += 1
print(ans)

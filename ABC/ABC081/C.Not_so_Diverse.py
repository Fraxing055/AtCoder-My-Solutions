N, K = map(int, input().split())
A = list(map(int, input().split()))
D = {}

for i in range(N):
  if A[i] in D:
    D[A[i]] += 1
  else:
    D[A[i]] = 1

Ds = dict(sorted(D.items(), key=lambda x:x[1], reverse=True))
Ns = len(Ds)
val = list(Ds.values())

count, ans = 1, 0

for k in range(Ns):
  if count > K:
    ans += val[k]
  else:
    count += 1
print(ans)

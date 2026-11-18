N, K = map(int, input().split())
A = list(map(int, input().split()))

def check(X):
  total = 0
  for idx in range(N):
    i = idx + 1
    if A[idx] < X:
      need = (X - A[idx] + i - 1) // i
      total += need
      if total > K:
        return False
  return True

ok = min(A)
ng = 10 ** 25

while ng - ok > 1:
  mid = (ok + ng) // 2
  if check(mid):
    ok = mid
  else:
    ng = mid
print(ok)

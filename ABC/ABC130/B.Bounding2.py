from bisect import bisect_right

N, X = map(int, input().split())
L = list(map(int, input().split()))
S = [0]
for i in range(N):
  S.append(S[-1] + L[i])
ans = bisect_right(S, X)
print(ans)

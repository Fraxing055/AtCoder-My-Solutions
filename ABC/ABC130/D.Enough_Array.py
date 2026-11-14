from bisect import bisect_left, bisect_right

N, K = map(int, input().split())
A = list(map(int, input().split()))
S = [0]
for i in range(N):
  S.append(S[-1] + A[i])
ans = 0
for l in range(N):
  idx = bisect_left(S, S[l] + K)
  ans += N - idx + 1
print(ans)

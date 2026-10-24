N, K, Q = map(int, input().split())

lst = [0] * N

for _ in range(Q):
  A = int(input())
  lst[A-1] += 1

for i in range(N):
  cal = K - Q + lst[i]
  if cal > 0:
    print('Yes')
  else:
    print('No')

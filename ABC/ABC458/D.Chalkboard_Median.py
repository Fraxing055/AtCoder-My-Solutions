import heapq

X = int(input())
Q = int(input())
high = []
low = []

def add(k):
  heapq.heappush(low, k *(-1))
  heapq.heappush(high, (-1) * low[0])
  heapq.heappop(low)
  if len(high) > len(low):
    heapq.heappush(low, (-1) * high[0])
    heapq.heappop(high)

add(X)

for _ in range(Q):
  A, B = map(int, input().split())
  add(A)
  add(B)
  print(low[0] * (-1))

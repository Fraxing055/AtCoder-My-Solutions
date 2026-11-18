from bisect import bisect_left

N = int(input())
lst = []
for _ in range(N):
  data = list(map(int, input().split()))
  lst.append(data)
Lst = []
maxH = 0
for i in range(N-1, -1, -1):
  if maxH < lst[i][0]:
    Lst.append(lst[i])
    maxH = lst[i][0]
Lst.reverse()

Q = int(input())
query = list(map(int, input().split()))
for q in query:
  ans = bisect_left(Lst, q + 0.5, key=lambda item: item[1])
  print(Lst[ans][0])

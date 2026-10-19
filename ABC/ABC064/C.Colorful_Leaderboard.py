N = int(input())
A = list(map(int, input().split()))
rank = []

for i in range(N):
  cal = A[i] // 400
  rank.append(cal)

inranks = len({x for x in rank if x < 8})
outranks = sum(y > 7 for y in rank)

if inranks == 0:
  minans = 1
  maxans = outranks
else:
  minans = inranks
  maxans = inranks + outranks

print(minans, maxans)

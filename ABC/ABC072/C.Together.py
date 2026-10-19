from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cand = []
for a in A:
  cand.append(a - 1)
  cand.append(a)
  cand.append(a + 1)

count = Counter(cand)
print(max(count.values()))

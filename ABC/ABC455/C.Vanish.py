N, K = map(int, input().split())
A = list(map(int, input().split()))
D = {}

for a in A:
  if a in D:
    D[a] += 1
  else:
    D[a] = 1
lst = []
for k in D:
  lst.append(int(k) * int(D[k]))
lst.sort(reverse=True)
print(sum(lst[K:]) if len(D) > K else 0) 

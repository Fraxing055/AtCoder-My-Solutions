N = int(input())
D = {}

for i in range(N):
  S = input()
  if S in D:
    D[S] += 1
  else:
    D[S] = 1

check = max(D.values())
Ds = sorted(D.items(), key=lambda x:x[0])

for j in range(len(Ds)):
  if Ds[j][1] == check:
    print(Ds[j][0])

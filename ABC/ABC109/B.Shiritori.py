N = int(input())
D = {}

for i in range(N):
  W = input()
  F, E = W[0], W[-1]
  if i != 0:
    if provE != F:
      print('No')
      break
  if W in D:
    print('No')
    break
  else:
    D[W] = 1
    provE = E
else:
  print('Yes')

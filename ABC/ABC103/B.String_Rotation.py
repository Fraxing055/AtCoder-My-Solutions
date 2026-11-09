S = list(input())
T = list(input()) * 2

N = len(S)

for i in range(N):
  num = 0
  for j in range(i,N+i):
    if S[num] == T[j]:
      num += 1
    else:
      break
  else:
    print('Yes')
    break
else:
  print('No')

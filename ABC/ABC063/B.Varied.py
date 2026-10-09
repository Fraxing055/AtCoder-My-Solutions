S = input()
N = len(S)
lst = list(S)
K = True
for i in range(N):
  for j in range(i+1, N):
    if lst[i] == lst[j]:
      print('no')
      K = False
      break
  if K == False:
    break
else:
  print('yes')

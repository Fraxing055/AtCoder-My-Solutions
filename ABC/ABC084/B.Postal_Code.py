A, B = map(int, input().split())
S = list(input())

flag = False

for a in range(A):
  try:
    K = int(S[a])
  except:
    print('No')
    break
else:
  if S[A] != '-':
    print('No')
  else:
    for b in range(A+1, A+B+1):
      try:
         K = int(S[b])
      except:
        print('No')
        break
    else:
      print('Yes')

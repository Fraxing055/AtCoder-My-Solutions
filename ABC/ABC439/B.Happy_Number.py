N = int(input())
lst = [N]

while N != 1:
  n = len(str(N))
  l = list(str(N))
  ans = 0
  for i in range(n):
    ans += int(l[i]) ** 2
  if ans in lst:
    break
  else:
    lst.append(N)
    N = ans
if N == 1:
  print('Yes')
else:
  print('No')
  

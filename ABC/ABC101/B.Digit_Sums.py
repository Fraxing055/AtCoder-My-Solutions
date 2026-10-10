N = input()
lst = [int(n) for n in N]
N = int(N)

if N % sum(lst) == 0:
  print('Yes')
else:
  print('No')

N = int(input())
A = list(map(int, input().split()))

Nontimes = 0
Secondtimes = 0
Forthtimes = 0

for i in range(N):
  if A[i] % 4 == 0:
    Forthtimes += 1
  elif A[i] % 2 == 0:
    Secondtimes += 1
  else:
    Nontimes += 1

if Secondtimes == 0:
  print('Yes' if Nontimes <= Forthtimes + 1 else 'No')
else:
  print('Yes' if Nontimes <= Forthtimes else 'No')

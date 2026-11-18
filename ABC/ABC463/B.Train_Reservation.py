N, X = map(str, input().split())
N = int(N)

for _ in range(N):
  S = list(input())
  if X == 'A' and S[0] == 'o':
    print("Yes")
    break
  elif X == 'B' and S[1] == 'o':
    print("Yes")
    break
  elif X == 'C' and S[2] == 'o':
    print("Yes")
    break
  elif X == 'D' and S[3] == 'o':
    print("Yes")
    break
  elif X == 'E' and S[4] == 'o':
    print("Yes")
    break
else:
  print("No")

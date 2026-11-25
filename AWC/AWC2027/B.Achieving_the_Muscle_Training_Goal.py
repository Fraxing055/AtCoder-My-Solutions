H, W = map(int, input().split())

for i in range(H):
  S = input()
  for j in range(W):
    if S[j] == 'o':
      print(j+1)
      break
  else:
    print(-1)

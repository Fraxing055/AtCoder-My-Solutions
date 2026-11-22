N = int(input())
S = input()

for i in range(N):
  if S[i] == 'z':
    print(i+1)
    break
else:
  print(-1)

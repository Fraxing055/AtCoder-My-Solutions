S = input()
N = len(S)
Red, Blue = 0, 0

for i in range(N):
  if S[i] == "0":
    Red += 1
  else:
    Blue += 1
if Red == N or Blue == N:
  print(0)
else:
  print(N - abs(Red - Blue))

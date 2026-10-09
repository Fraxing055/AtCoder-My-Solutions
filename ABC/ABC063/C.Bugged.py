N = int(input())
S = []
Mod10 = []
for _ in range(N):
  s = int(input())
  S.append(s)
S.sort()
for i in range(N):
  cal = S[i] % 10
  Mod10.append(cal)

if sum(S) % 10 != 0:
  print(sum(S))
elif sum(Mod10) == 0:
  print(0)
else:
  for j in range(N):
    if Mod10[j] != 0:
      print(sum(S) - S[j])
      break

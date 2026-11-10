N, M = map(int, input().split())
lst = []
for _ in range(M):
  sc = list(map(int, input().split()))
  lst.append(sc)
anslst = [0] * N
F = False

for i in range(M):
  for j in range(i, M):
    if lst[i][0] == lst[j][0] and lst[i][1] != lst[j][1]:
      print(-1)
      F = True
      break
    if N > 1 and ((lst[i][0] == 1 and lst[i][1] == 0) or (lst[j][0] == 1 and lst[j][1] == 0)):
      print(-1)
      F = True
      break
    if lst[i][0] > N or lst[j][0] > N:
      print(-1)
      F = True
      break
  if F == True:
    break
else:
  for k in range(M):
    anslst[lst[k][0]-1] = lst[k][1]
  if N > 1 and anslst[0] == 0:
    anslst[0] = 1
  print("".join([str(x) for x in anslst]))

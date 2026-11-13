N, M = map(int, input().split())
Loserlst = []
ans = -1

for _ in range(M):
  A, B = map(int, input().split())
  Loserlst.append(B)
for i in range(1,N+1):
  if not i in Loserlst:
    if ans == -1:
      ans = i
    else:
      ans = -1
      break
print(ans)

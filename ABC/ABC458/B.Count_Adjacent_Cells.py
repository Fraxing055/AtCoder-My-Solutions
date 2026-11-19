H, W = map(int, input().split())

if H == 1 and W == 1:
  print(0)
  exit()
if H == 1 and W != 1:
  ans = []
  ans.append("1")
  for _ in range(W-2):
    ans.append("2")
  ans.append("1")
  print(" ".join(ans))
  exit()
if H != 1 and W == 1:
  print(1)
  for _ in range(H-2):
    print(2)
  print(1)
  exit()

ans = []

for i in range(H):
  cal = []
  for j in range(W):
    if (i == 0 or i == H-1) and (j == 0 or j == W-1):
      cal.append("2")
    elif (i == 0 or i == H-1) or (j == 0 or j == W-1):
      cal.append("3")
    else:
      cal.append("4")
  ans.append(cal)
for k in range(H):
  print(" ".join(ans[k]))

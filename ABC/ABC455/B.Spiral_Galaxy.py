H, W = map(int, input().split())
gd = []
for _ in range(H):
  gd.append(list(input()))

ans = 0

for i in range(H):
  for j in range(W):
    for k in range(i, H):
      for l in range(j, W):
        checkLow = (k - i + 2) // 2
        F = True
        for m in range(checkLow):
          for n in range(l-j+1):
            if gd[i+m][j+n] != gd[k-m][l-n]:
              F = False
              break
          if F == False:
            break
        else:
          ans += 1
print(ans)

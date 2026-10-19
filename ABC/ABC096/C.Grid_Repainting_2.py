H, W = map(int, input().split())
grid = [input() for _ in range(H)]

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
flag = False

for i in range(H):
  ans = []
  for j in range(W):
    if grid[i][j] == '.':
      continue
    else:
      for k in range(4):
        if 0 <= j + dx[k] < W and 0 <= i + dy[k] < H:
          if grid[i + dy[k]][j + dx[k]] == '#' :
            break
      else:
        flag = True
        break
  if flag == True:
    print('No')
    break
else:
  print('Yes')

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(H):
  ans = []
  for j in range(W):
    if grid[i][j] == '#':
      ans.append('#')
    else:
      count = 0
      for k in range(8):
        if 0 <= j + dx[k] < W and 0 <= i + dy[k] < H:
          if grid[i + dy[k]][j + dx[k]] == '#' :
            count += 1
      ans.append(count)
  print("".join(map(str, ans)))
  

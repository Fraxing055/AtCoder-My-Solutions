H, W = map(int, input().split())
grid = [input() for _ in range(H)]

row_ok = ['#' in row for row in grid]

col_ok = [any(grid[i][j] == '#' for i in range(H)) for j in range(W)]

for i in range(H):
    if not row_ok[i]:
        continue
    line = []
    for j in range(W):
        if col_ok[j]:
            line.append(grid[i][j])
    print("".join(line))

N = int(input())
point = [[0, 0, 0]]
for _ in range(N):
    point.append(list(map(int, input().split())))

for i in range(N):
    dt = point[i + 1][0] - point[i][0]
    dist = abs(point[i][1] - point[i + 1][1]) + abs(point[i][2] - point[i + 1][2])

    if dist > dt or (dt - dist) % 2 != 0:
        print("No")
        break
else:
    print("Yes")

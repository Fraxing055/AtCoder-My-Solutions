import sys
input = sys.stdin.readline  

N, M = map(int, input().split())
ans = 0
cakes = []
for _ in range(N):
    x, y, z = map(int, input().split())
    cakes.append((x, y, z))

signs = [-1, 1]
for sx in signs:
  for sy in signs:
    for sz in signs:
      scores = []
      for x, y, z in cakes:
        score = sx * x + sy * y + sz * z
        scores.append(score)
      scores.sort(reverse=True)
      c_sum = sum(scores[:M])
      if c_sum > ans:
        ans = c_sum

print(ans)

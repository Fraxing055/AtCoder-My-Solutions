N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(M)]

ab.sort(key=lambda x: x[1])

ans = 0
last = 0

for a, b in ab:
  if last < a:
      ans += 1
      last = b - 1
print(ans)

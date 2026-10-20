R, G, B, N = map(int, input().split())
X, Y, Z = sorted([R, G, B], reverse=True)
ans = 0

for x in range(N // X + 1):
  rem = N - X * x
  for y in range(rem // Y + 1):
    remain = rem - Y * y
    if remain % Z == 0:
      ans += 1
print(ans)

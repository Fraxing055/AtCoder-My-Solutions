N = int(input())
A = list(map(int, input().split()))
ans = 0

for i in range(N):
  cal = A[i]
  while True:
    if cal % 2 == 0:
      ans += 1
      cal = cal // 2
    else:
      break
print(ans)

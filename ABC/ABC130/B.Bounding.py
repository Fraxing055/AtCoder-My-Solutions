N, X = map(int, input().split())
L = list(map(int, input().split()))

ans = 1
B = 0
for i in range(N):
  if L[i] + B <= X:
    ans += 1
    B += L[i]
  else:
    break
print(ans)

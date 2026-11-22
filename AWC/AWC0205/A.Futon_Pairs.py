N = int(input())
ans = []
for _ in range(N):
  A, B = map(int, input().split())
  ans.append('o' if (A + B) % 2 == 0 else 'x')
print("".join(ans))

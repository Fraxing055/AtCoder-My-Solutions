N = int(input())
L = []
for _ in range(N):
  L.append(list(map(int, input().split())))
X, Y = map(int, input().split())

print(L[X-1][Y])

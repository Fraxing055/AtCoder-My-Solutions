N = int(input())
Chack = []
anslst = []

for _ in range(N):
  C = int(input())
  A = list(map(int, input().split()))
  Chack.append(A)
X = int(input())
M = 40
for i in range(1, N+1):
  if X in Chack[i-1]:
    if len(Chack[i-1]) == M:
      anslst.append(i)
    elif len(Chack[i-1]) < M:
      M = len(Chack[i-1])
      anslst = [i]
print(len(anslst))
print(*anslst)

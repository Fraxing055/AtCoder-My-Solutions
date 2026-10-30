N, M = map(int, input().split())

anslst = [0] * N

for _ in range(M):
  A, B = map(int, input().split())
  anslst[A-1] += 1
  anslst[B-1] += 1

for i in range(N):
  print(anslst[i])

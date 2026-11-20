N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

final = 0

for i in range(N):
  answer = 0
  for j in range(M):
    answer += A[i][j] * B[j]
  answer += C
  if answer > 0:
    final += 1
print(final)

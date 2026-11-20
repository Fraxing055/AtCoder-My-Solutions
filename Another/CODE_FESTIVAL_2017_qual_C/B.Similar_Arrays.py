N = int(input())
A = list(map(int, input().split()))

ALL = 3 ** N
odds = 1
for i in range(N):
  if A[i] % 2 == 0:
    odds *= 2
print(ALL - odds)

N = int(input())
A = list(map(int, input().split()))
S = sum(A)
Avg = S // N
Upper, Lower = 0, 0

for i in range(N):
  if A[i] > Avg + 1:
    Upper += A[i] - (Avg + 1)
  else:
    Lower += Avg - A[i]
print(max(Upper, Lower))

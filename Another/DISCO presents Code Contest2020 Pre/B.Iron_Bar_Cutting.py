N = int(input())
A = list(map(int, input().split()))

if N == 2:
  print(abs(A[0] - A[-1]))
  exit()

left = A[0]
right = A[-1]
i, j = 0, 0
for _ in range(N-3):
  if left <= right:
    i += 1
    left += A[i]
  else:
    j += 1
    right += A[-1-j]
print(abs(abs(left - right) - A[i+1]))
  

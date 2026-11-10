N = int(input())
A = list(map(int, input().split()))
ans = 1
state = 0

for i in range(N-1):
  if A[i] < A[i+1]:
    if state == -1:
      ans += 1
      state = 0
    elif state == 0:
      state = 1
  elif A[i] > A[i+1]:
    if state == 1:
      ans += 1
      state = 0
    elif state == 0:
      state = -1
print(ans)

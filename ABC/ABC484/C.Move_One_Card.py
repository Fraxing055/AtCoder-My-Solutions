N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

F = False

for i in range(N):
  if A[i] != B[i]:
    for j in range(N-1, i-1, -1):
      if A[j] != B[j]:
        if A[i:j] == B[i+1:j+1] and A[j] == B[i]:
          print('Yes')
          F = True
          break
        elif B[i:j] == A[i+1:j+1] and B[j] == A[i]:
          print('Yes')
          F = True
          break
        else:
          print('No')
          F = True
          break
  if F == True:
    break
else:
  print('Yes')

S = list(input())
N = len(S)
Rlist = [0] * N
Llist = [0] * N
ans = [0] * N

C = 0
for i in range(N-1):
  if S[i] == 'R' and S[i+1] == 'R':
    C += 1
  elif S[i] == 'R' and S[i+1] == 'L':
    C += 1
    Rlist[i] = (C + 1) // 2
    Rlist[i+1] = C - Rlist[i]
    C = 0
C = 0
for j in range(N-1, 0, -1):
  if S[j] == 'L' and S[j-1] == 'L':
    C += 1
  elif S[j] == 'L' and S[j-1] == 'R':
    C += 1
    Llist[j] = (C + 1) // 2
    Llist[j-1] = C - Llist[j]
    C = 0
for k in range(N):
  ans[k] = Rlist[k] + Llist[k]
print(*ans)
  

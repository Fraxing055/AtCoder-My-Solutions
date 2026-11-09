S = list(input())
N = len(S)

Ap = 0
Zp = len(S) + 1
ans = 0

for i in range(N):
  if S[i] == 'A':
    Ap = i
    break
for j in range(N-1, 0, -1):
  if S[j] == 'Z':
    Zp = j
    break
print(Zp - Ap + 1)

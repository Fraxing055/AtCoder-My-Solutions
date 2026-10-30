A, B, K = map(int, input().split())

ans = []

for _ in range(K):
  cal = A
  if A == B:
    ans.append(B)
    break
  ans.append(A)
  A += 1
else:
  lim = A - 1
  for _ in range(K):
    cal = B
    if B == lim:
      break
    ans.append(B)
    B -= 1

ans.sort()

for i in range(len(ans)):
  print(ans[i])

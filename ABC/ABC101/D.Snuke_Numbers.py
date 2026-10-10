K = int(input())

ans = 1
d = 1

for _ in range(K):
  print(ans)
  
  cand1 = ans + d
  s1 = sum(int(c) for c in str(cand1))
  cand2 = ans + 10 * d
  s2 = sum(int(c) for c in str(cand2))
  
  if cand1 * s2 > cand2 * s1:
    d *= 10
    ans += d
  else:
    ans += d

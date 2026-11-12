from collections import Counter
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

R = Counter(A)
L = defaultdict(int)
ans = 0

for j in range(0,N):
  Aj = A[j]
  R[Aj] -= 1
  if Aj%5 == 0:
    k = Aj // 5
    ans += R[7 * k] * R[3 * k]
    ans += L[7 * k] * L[3 * k]
  L[Aj] += 1
print(ans)
  

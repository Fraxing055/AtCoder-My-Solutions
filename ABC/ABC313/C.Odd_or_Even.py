N, K = map(int, input().split())
S = []
First = list(range(1, K+2))

for i in range(K+1):
  Q1 = [str(x) for j, x in enumerate(First) if j != i]
  print("?", *Q1, flush=True)
  S.append(int(input()))
T = sum(S) % 2
ans = [T ^ s for s in S]

Bq = [str(x) for x in range(1, K)]
Bp = sum(ans[:K-1]) % 2

for m in range(K + 2, N + 1):
    print("?", *Bq, m, flush=True)
    d = int(input())
    ans.append(Bp ^ d)

print("!", *ans, flush=True)

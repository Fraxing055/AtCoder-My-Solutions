S = list(input())
N = len(S)

ans = 10 ** 4

for i in range(N-2):
  cal = 100 * int(S[i]) + 10 * int(S[i+1]) + int(S[i+2])
  cal = abs(753 - cal)
  ans = min(ans, cal)
print(ans)

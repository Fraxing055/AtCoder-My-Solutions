S = input()
N = len(S)

ans1 = 0
for i in range(N):
  if i % 2 == 0 and S[i] == '1':
    ans1 += 1
  elif i % 2 == 1 and S[i] == '0':
    ans1 += 1

ans2 = N - ans1

print(min(ans1, ans2))

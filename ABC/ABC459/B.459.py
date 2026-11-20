N = int(input())
S = list(map(str, input().split()))
ans = []

for i in range(N):
  if S[i][0] in ['a', 'b', 'c']:
    ans.append('2')
  elif S[i][0] in ['d', 'e', 'f']:
    ans.append('3')
  elif S[i][0] in ['g', 'h', 'i']:
    ans.append('4')
  elif S[i][0] in ['j', 'k', 'l']:
    ans.append('5')
  elif S[i][0] in ['m', 'n', 'o']:
    ans.append('6')
  elif S[i][0] in ['p', 'q', 'r', 's']:
    ans.append('7')
  elif S[i][0] in ['t', 'u', 'v']:
    ans.append('8')
  else:
    ans.append('9')
print("".join(ans))

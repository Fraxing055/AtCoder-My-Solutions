S = input()

target = 'keyence'

for i in range(8):
  if S[:i] + S[len(S) - (7 - i) :] == target:
    print('YES')
    break
else:
  print('NO')

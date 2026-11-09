s = list(input())

Np, Sp, Ep, Wp = 0, 0, 0, 0

if 'N' in s:
  Np = 1
if 'S' in s:
  Sp = 1
if 'E' in s:
  Ep = 1
if 'W' in s:
  Wp = 1

print('No' if (Np != Sp or Ep != Wp) else 'Yes')

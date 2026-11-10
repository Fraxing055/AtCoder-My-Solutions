S = list(input())
T = list(input())
Ns, Nt = len(S), len(T)
Nc = min(Ns, Nt)

SS = sorted(S)
ST = sorted(T, reverse = True)

A = SS[:Nc]
B = ST[:Nc]
if A == B:
  if Ns >= Nt:
    print("No")
  else:
    print("Yes")
else:
  if A > B:
    print("No")
  else:
    print("Yes")

from collections import Counter

S = input()
lst = list(S)
N = len(lst)
wlst = lst[2:N-1]

cl = Counter(lst)
cw = Counter(wlst)

if S[0] != "A":
  print('WA')
elif cl["C"] != cw["C"] or cw["C"] != 1:
  print("WA")
else:
  lst.remove("A")
  lst.remove("C")
  if all(l.islower() for l in lst):
    print("AC")
  else:
    print("WA")

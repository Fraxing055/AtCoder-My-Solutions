import collections
import sys

w = list(input())
lst = collections.Counter(w)
print(f'DBG : {lst=}', file=sys.stderr)

for v in lst.values():
  if v % 2 != 0:
    print('No')
    break
else:
  print('Yes')

from collections import Counter

s = int(input())
lst = []
lst.append(s)
ct = 1

while True:
  if s % 2 == 0:
    s = s // 2
  else:
    s = 3 * s + 1
  lst.append(s)
  ct += 1
  counter = Counter(lst)
  if max(counter.values()) >= 2:
    print(ct)
    break

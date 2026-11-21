lst = list(map(int, input().split()))

rem = 0
for i in range(len(lst)):
  rem += max(lst) - lst[i]
if rem % 2 == 0:
  print(rem // 2)
else:
  print((rem + 3) // 2)

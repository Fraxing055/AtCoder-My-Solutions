a, b = map(int, input().split())
high = max(a, b)
low = min(a, b)

if high == low:
  if high > 0:
    print('Positive')
  elif high == 0:
    print('Zero')
  else:
    print('Negative')
elif 0 < low:
  print('Positive')
elif low <= 0 and 0 <= high:
  print('Zero')
else:
  cal = high - low + 1
  if cal % 2 == 0:
    print('Positive')
  else:
    print('Negative')

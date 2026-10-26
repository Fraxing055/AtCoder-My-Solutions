A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))

ans = 0

for i in range(6):
  for j in range(6):
    for k in range(6):
      if A1[i] == 4 and A2[j] == 5 and A3[k] == 6:
        ans += 1
      elif A1[i] == 4 and A2[j] == 6 and A3[k] == 5:
        ans += 1
      elif A1[i] == 5 and A2[j] == 4 and A3[k] == 6:
        ans += 1
      elif A1[i] == 5 and A2[j] == 6 and A3[k] == 4:
        ans += 1
      elif A1[i] == 6 and A2[j] == 4 and A3[k] == 5:
        ans += 1
      elif A1[i] == 6 and A2[j] == 5 and A3[k] == 4:
        ans += 1

print(ans / 216)

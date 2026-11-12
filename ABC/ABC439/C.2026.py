N = int(input())
count = 0
anslst = {}

for x in range(1, 10 ** 4):
  if x ** 2 > N / 2:
    break
  for y in range(x+1, 10 ** 4):
    cal = x ** 2 + y ** 2
    if cal > N:
      break
    if cal in anslst:
      anslst[cal] += 1
    else:
      anslst[cal] = 1
ans = [k for k, v in anslst.items() if v == 1]
ans.sort()
ans2 = [str(t) for t in ans]
print(len(ans2))
print(" ".join(ans2))

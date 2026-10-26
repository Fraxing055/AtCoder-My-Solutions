N = int(input())

dic = {}

for _ in range(N):
  S = input()
  lst = list(S)
  lst = sorted(S)
  Sn = "".join(lst)
  
  if Sn in dic:
    dic[Sn] += 1
  else:
    dic[Sn] = 0

ans = 0

for i in dic:
  if dic[i] != 0:
    cal = dic[i] + 1
    ans += cal * (cal - 1) // 2

print(ans)

N, M = map(int, input().split())
student = []
check = []
for _ in range(N):
  student.append(list(map(int, input().split())))
for _ in range(M):
  check.append(list(map(int, input().split())))

for i in range(N):
  mindist = 10 ** 9
  ans = -1
  for j in range(M):
    cal = abs(student[i][0] - check[j][0]) + abs(student[i][1] - check[j][1])
    if mindist > cal:
      mindist = cal
      ans = j + 1
  print(ans)
  

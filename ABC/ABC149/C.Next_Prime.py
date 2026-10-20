X = int(input())
flag = False

while flag == False:
  for i in range(2, X // 2 + 1):
    if X % i == 0:
      X += 1
      break
  else:
    print(X)
    flag = True

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

lst = [A, B, C, D, E]
diflst = []

for i in range(5):
  if lst[i] % 10 == 0:
    diflst.append(0)
  else:
    dif = 10 - (lst[i] % 10)
    lst[i] = lst[i] + dif
    diflst.append(dif)
print(sum(lst) - max(diflst))

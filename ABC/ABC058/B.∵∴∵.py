O = list(input())
E = list(input())
anslst = []

if len(O) == len(E):
  for i in range(len(O)):
    anslst.append(O[i])
    anslst.append(E[i])
else:
  for i in range(len(O) - 1):
    anslst.append(O[i])
    anslst.append(E[i])
  anslst.append(O[-1])
print("".join(anslst))

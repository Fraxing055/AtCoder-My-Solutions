N, M = map(int, input().split())
F = False
for i in range(N):
  S = list(input())
  if S[0] == S[1] and S[1] == "x":
    print(f"Faucet {i+1}")
    break
  else:
    for j in range(M):
      if S[j] == "x":
        print(f"Drain {j+1}")
        F = True
        break
  if F == True:
    break
  

N = int(input())
s = list(input())
t = list(input())

if s == t:
  print(N)
else:
  dist = N
  for k in range(N):
    if s[k:] == t[:(N-k)]:
      dist = min(k, dist)
  print(N + dist)

      

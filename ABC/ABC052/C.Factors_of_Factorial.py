N = int(input())
MOD = 10**9 + 7

count = [0] * (N + 1)

for i in range(1, N + 1):
    x = i
    d = 2
    while d * d <= x:
        while x % d == 0:
            count[d] += 1
            x //= d
        d += 1
    if x > 1:
        count[x] += 1

ans = 1
for c in count:
    if c > 0:
        ans = (ans * (c + 1)) % MOD

print(ans)

from collections import Counter

N = int(input())
A = list(map(int, input().split()))
ans = 0

counts = Counter(A)

for x, cal in counts.items():
    if x != cal:
        if x > cal:
            ans += cal
        else:
            ans += cal - x

print(ans)

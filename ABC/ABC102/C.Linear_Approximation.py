N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(N):
    B.append(A[i] - (i + 1))

B.sort()

b = B[N // 2]

ans = 0
for j in B:
    ans += abs(j - b)

print(ans)

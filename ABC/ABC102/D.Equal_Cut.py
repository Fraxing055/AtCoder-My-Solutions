import bisect

N = int(input())
A = list(map(int, input().split()))


S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

ans = float('inf')


for mid in range(2, N - 1):
    sum_left = S[mid]          
    sum_right = S[N] - S[mid]  

    target_left = sum_left / 2
    idx_l = bisect.bisect_left(S, target_left, 1, mid)
    best_l = idx_l
    if idx_l > 1 and abs(S[idx_l - 1] - target_left) < abs(S[idx_l] - target_left):
        best_l = idx_l - 1

    P = S[best_l]
    Q = sum_left - P

    target_right = S[mid] + sum_right / 2
    idx_r = bisect.bisect_left(S, target_right, mid + 1, N)
    best_r = idx_r
    if idx_r > mid + 1 and abs(S[idx_r - 1] - target_right) < abs(S[idx_r] - target_right):
        best_r = idx_r - 1

    R = S[best_r] - S[mid]
    S_part = S[N] - S[best_r]

    diff = max(P, Q, R, S_part) - min(P, Q, R, S_part)
    if diff < ans:
        ans = diff

print(ans)

N, K = map(int, input().split())
P = list(map(int, input().split()))

cur = sum(P[:K])
ans = cur


for i in range(K, N):
    cur += P[i]      
    cur -= P[i - K]  
    if cur > ans:
        ans = cur

print((ans + K) / 2)

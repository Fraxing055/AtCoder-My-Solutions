import math

N = int(input())

ans = 0
two_pow = 2 

while two_pow <= N:
    M = N // two_pow
    max_c = math.isqrt(M)
    
    ans += (max_c + 1) // 2
    
    two_pow *= 2

print(ans)

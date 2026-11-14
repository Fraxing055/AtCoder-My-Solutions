import math

A, B, C, D = map(int, input().split())
CD = math.lcm(C, D)

def f(X):
    return X - (X // C) - (X // D) + (X // CD)

print(f(B) - f(A - 1))

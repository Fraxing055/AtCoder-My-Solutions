N, A, B = map(int, input().split())
C = A - B
H = [int(input()) for _ in range(N)]

Lower = 0
Upper = (max(H) + B - 1) // B

while Lower < Upper:
    k = (Lower + Upper) // 2
    need = 0
    for h in H:
      rem = h - B * k
      if rem > 0:
        need += (rem + C - 1) // C
    if need <= k:
      Upper = k
    else:
      Lower = k + 1
print(Lower)

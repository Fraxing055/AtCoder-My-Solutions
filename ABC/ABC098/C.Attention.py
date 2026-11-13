N = int(input())
S = input()

Left = 0
Right = S.count('E')
ans = N

for c in S:
    if c == 'E':
        Right -= 1  
    ans = min(ans, Left + Right)
    if c == 'W':
        Left += 1   

print(ans)

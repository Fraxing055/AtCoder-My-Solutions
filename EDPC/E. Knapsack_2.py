import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    W = int(input_data[1])
    V = 1000 * N

    dp = [[10**18] * (V + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    idx = 2
    for i in range(1, N + 1):
        weight = int(input_data[idx])
        value = int(input_data[idx + 1])
        idx += 2

        for v in range(V + 1):
            dp[i][v] = dp[i - 1][v]

            if v >= value:
                candidate = dp[i - 1][v - value] + weight
                if candidate < dp[i][v]:
                    dp[i][v] = candidate

    ans = 0
    for v in range(V, -1, -1):
        if dp[N][v] <= W:
            ans = v
            break

    print(ans)


if __name__ == "__main__":
    solve()

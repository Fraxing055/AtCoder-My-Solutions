import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    W = int(input_data[1])

    dp = [[0] * (W + 1) for _ in range(N + 1)]

    idx = 2
    for i in range(1, N + 1):
        weight = int(input_data[idx])
        value = int(input_data[idx + 1])
        idx += 2

        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]

            if w >= weight:
                candidate = dp[i - 1][w - weight] + value
                if candidate > dp[i][w]:
                    dp[i][w] = candidate

    print(max(dp[N]))


if __name__ == "__main__":
    solve()

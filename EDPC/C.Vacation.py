import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])

    dp = [int(input_data[1]), int(input_data[2]), int(input_data[3])]

    idx = 4
    for _ in range(1, N):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        c = int(input_data[idx + 2])
        idx += 3

        new_dp0 = max(dp[1], dp[2]) + a
        new_dp1 = max(dp[0], dp[2]) + b
        new_dp2 = max(dp[0], dp[1]) + c

        dp = [new_dp0, new_dp1, new_dp2]

    print(max(dp))


if __name__ == "__main__":
    solve()
  

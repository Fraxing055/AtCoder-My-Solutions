import sys


def solve():
    lines = sys.stdin.read().split()
    if not lines:
        return
    s = lines[0]
    t = lines[1]

    n = len(s)
    m = len(t)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 1. 端の初期化（空文字列からの削除・挿入コスト）
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # 2. テーブルの更新
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                # 一致：コストなしで斜めから引き継ぐ
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # 不一致：置換(斜め), 削除(上), 挿入(左) の最小値 + 1
                dp[i][j] = (
                    min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                )

    print(dp[-1][-1])


if __name__ == "__main__":
    solve()

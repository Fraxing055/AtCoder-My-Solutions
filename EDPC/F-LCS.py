import sys


def solve():
    # 入力取得
    lines = sys.stdin.read().split()
    if not lines:
        return
    s = lines[0]
    t = lines[1]

    n = len(s)
    m = len(t)

    # 1. テーブル作成（数値の最大長だけを計算）
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 2. 型流用：ゴール (n, m) から逆走して文字を回収
    ans = []
    i, j = n, m
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            ans.append(s[i - 1])  # 一致した文字を回収
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1  # 上から引き継いだ
        else:
            j -= 1  # 左から引き継いだ

    # 逆順にして出力
    print("".join(reversed(ans)))


if __name__ == "__main__":
    solve()

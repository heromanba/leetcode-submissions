class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [
            [0 for _ in range(n)]
            for _ in range(m)
        ]
        dp[-1][-1] = 1
        for offset in range(1, m-1+n-1+1):
            # m-1-i + n-1-j == offset
            # i + j = m-1+n-1-offset
            # j = (m-1+n-1-offset) - i
            # 0 <= (m-1+n-1-offset) - i <= n-1
            lower = max(0, m-1-offset)
            upper = min(m-1, m-1+n-1-offset)
            for i in range(lower, upper+1):
                j = (m-1+n-1-offset) - i
                if i+1<=m-1:
                    dp[i][j] += dp[i+1][j]
                if j+1<=n-1:
                    dp[i][j] += dp[i][j+1]
        return dp[0][0]

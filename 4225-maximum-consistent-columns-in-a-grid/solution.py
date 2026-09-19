class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        max_cols = 0
        dp = [1] * len(grid[0])
        for i in range(len(grid[0])):
            for j in range(i):
                consistent = True
                for k in range(len(grid)):
                    if abs(grid[k][i]-grid[k][j]) > limit:
                        consistent = False
                        break
                if consistent and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
            if dp[i] > max_cols:
                max_cols = dp[i]
        return max_cols


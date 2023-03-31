class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])

        row_max = [max(row) for row in grid]
        col_max = [max([row[i] for row in grid]) for i in range(n_col)]

        sum_v = 0
        for i in range(n_row):
            for j in range(n_col):
                sum_v += min(row_max[i], col_max[j]) - grid[i][j]
        
        return sum_v
        

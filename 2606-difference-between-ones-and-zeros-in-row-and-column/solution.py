class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ones_row = [ len([i for i in row if i == 1]) for row in grid ]
        zeros_row = [ len([i for i in row if i == 0]) for row in grid ]
        ones_col = [ len([row[col] for row in grid if row[col] == 1]) for col in range(len(grid[0])) ]
        zeros_col = [ len([row[col] for row in grid if row[col] == 0]) for col in range(len(grid[0])) ]
        diff = [None] * len(grid[0]) * len(grid)
        
        diff = [diff[i:i+len(grid[0])] for i in range(len(grid))]

        for i in range(len(diff)):
            for j in range(len(diff[0])):
                diff[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]
        return diff

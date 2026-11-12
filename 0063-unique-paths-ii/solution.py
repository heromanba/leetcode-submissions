class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        num_rows = len(obstacleGrid)
        num_cols = len(obstacleGrid[0])
        if obstacleGrid[num_rows-1][num_cols-1] == 1:
            return 0

        uniquePaths = [
            [0 for _ in range(num_cols)]
            for _ in range(num_rows)
        ]
        uniquePaths[num_rows-1][num_cols-1] = 1

        for distance in range(num_rows+num_cols-3, -1, -1):
            row_lower_limit = max(0, distance-(num_cols-1))
            row_upper_limit = min(distance, num_rows-1)
            for row in range(row_upper_limit, row_lower_limit-1, -1):
                col =  distance - row
                if obstacleGrid[row][col] == 1:
                    continue
                if row+1 <= num_rows-1:
                    uniquePaths[row][col] += uniquePaths[row+1][col]
                if col+1 <= num_cols-1:
                    uniquePaths[row][col] += uniquePaths[row][col+1]
        return uniquePaths[0][0]
                


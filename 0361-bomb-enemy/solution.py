class Solution:
    def maxKilledEnemies(self, grid: list[list[str]]) -> int:
        killed_enemies = [ 
            [0 for _ in range(len(grid[0]))] 
            for _ in range(len(grid))
        ]
        # sliding window each row
        for row in range(len(grid)):
            start = 0
            end = 0
            while True:
                num_enemies = 0
                while start < len(grid[0]) and grid[row][start] == 'W':
                    start += 1
                if start == len(grid[0]):
                    break
                end = start
                while end < len(grid[0]) and grid[row][end] != 'W':
                    if grid[row][end] == 'E':
                        num_enemies += 1
                    end += 1
                for col in range(start, end+1):
                    if col < len(grid[0]):
                        print(row, col, grid[row][col], num_enemies)
                    if col < len(grid[0]) and grid[row][col] == '0':
                        killed_enemies[row][col] = num_enemies
                if end == len(grid[0]):
                    break
                start = end + 1

        # sliding window each col
        for col in range(len(grid[0])):
            start = 0
            end = 0
            while True:
                num_enemies = 0
                while start < len(grid) and grid[start][col] == 'W':
                    start += 1
                if start == len(grid):
                    break
                end = start
                while end < len(grid) and grid[end][col] != 'W':
                    if grid[end][col] == 'E':
                        num_enemies += 1
                    end += 1
                for row in range(start, end+1):
                    if row < len(grid) and grid[row][col] == '0':
                        killed_enemies[row][col] += num_enemies
                if end == len(grid):
                    break
                start = end + 1
        
        max_killed_enemies = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_killed_enemies = max(max_killed_enemies, killed_enemies[i][j])
        return max_killed_enemies

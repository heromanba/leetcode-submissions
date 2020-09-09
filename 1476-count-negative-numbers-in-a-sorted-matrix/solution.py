class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        num_negative = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[-i][-j] < 0:
                    num_negative += 1
        return num_negative

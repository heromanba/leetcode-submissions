class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        
        def max_sub_sum_min_1(arr):
            max_sum = float('-inf')
            previous_max = None

            for i in range(len(arr)):
                if i == 0:
                    previous_max = arr[0]
                else:
                    previous_max = max(previous_max+arr[i], arr[i])
                max_sum = max(max_sum, previous_max)
                
            return max_sum
        
        def max_sub_sum_min_2(arr):
            max_sum = float('-inf')

            previous_sum = arr[0]

            for i in range(1, len(arr)):
                
                max_sum = max(max_sum, previous_sum + arr[i])

                previous_sum = max(previous_sum+arr[i], arr[i])

            return max_sum
        
        max_sum = float('-inf')

        # internal rows and cols allowed with min 1 length subarray
        for row_id in range(1, len(grid)-1):
            row = grid[row_id]
            print('row: ', row)
            max_sum = max(max_sum, max_sub_sum_min_1(row[1:-1]))

        for col_id in range(1, len(grid[0])-1):
            col = [grid[row_id][col_id] for row_id in range(len(grid))]
            print('col: ', col)
            max_sum = max(max_sum, max_sub_sum_min_1(col[1:-1]))

        # non-internal rows and cols allowed with min 2 length subarray
        for row_id in range(len(grid)):
            row = grid[row_id]
            max_sum = max(max_sum, max_sub_sum_min_2(row))

        for col_id in range(len(grid[0])):
            col = [grid[row_id][col_id] for row_id in range(len(grid))]
            max_sum = max(max_sum, max_sub_sum_min_2(col))

        return max_sum


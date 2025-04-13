class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        l = 0
        r = num_rows * num_cols - 1

        while l <= r:
            l_row = math.floor(l / num_cols)
            l_col = l % num_cols
            
            r_row = math.floor(r / num_cols)
            r_col = r % num_cols

            mid = math.floor(l + (r-l) / 2)
            mid_row = math.floor(mid / num_cols)
            mid_col = mid % num_cols

            if matrix[mid_row][mid_col] < target:
                l = mid + 1
            elif matrix[mid_row][mid_col] > target:
                r = mid - 1
            else:
                return True
        return False

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            has_zero = False
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    has_zero = True
                    break
            if has_zero:
                for col in range(len(matrix[0])):
                    if matrix[row][col] != 0:
                        matrix[row][col] = float('inf')

        for col in range(len(matrix[0])):
            has_zero = False
            for row in range(len(matrix)):
                if matrix[row][col] == 0:
                    has_zero = True
                    break
            if has_zero:
                for row in range(len(matrix)):
                    if matrix[row][col] != 0:
                        matrix[row][col] = float('inf')
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
        
        

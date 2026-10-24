class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.preprocessed = [
            [0 for _ in range(len(matrix[0]))] 
            for _ in range(len(matrix))
        ]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                prefix_sum = matrix[i][j]
                if i > 0:
                    prefix_sum += self.preprocessed[i-1][j]
                if j > 0:
                    prefix_sum += self.preprocessed[i][j-1]
                if i > 0 and j > 0:
                    prefix_sum -= self.preprocessed[i-1][j-1]
                self.preprocessed[i][j] = prefix_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_sum = self.preprocessed[row2][col2]
        if col1-1 >= 0:
            region_sum -= self.preprocessed[row2][col1-1]
        if row1-1 >= 0:
            region_sum -= self.preprocessed[row1-1][col2]
        if col1-1 >= 0 and row1-1>=0:
            region_sum += self.preprocessed[row1-1][col1-1]
        return region_sum
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

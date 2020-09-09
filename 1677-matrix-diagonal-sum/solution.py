class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag_sum = 0
        for i in range(len(mat)):
            diag_sum += mat[i][i]
            j = len(mat) - i -1
            if i != j:
                diag_sum += mat[i][j]
        return diag_sum

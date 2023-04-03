class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # iterate over all diagonal starting pt
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # just first row and col
                if i != 0 and j != 0:
                    break
                # find pts on the diagonal
                diag = []
                d_i, d_j = 0, 0
                while (i+d_i < len(mat)) and (j+d_j < len(mat[0])):
                    diag.append(mat[i+d_i][j+d_j])
                    d_i += 1
                    d_j += 1
                diag.sort(reverse=True)
                d_i, d_j = 0, 0
                while (i+d_i < len(mat)) and (j+d_j < len(mat[0])):
                    mat[i+d_i][j+d_j] = diag.pop()
                    d_i += 1
                    d_j += 1
        # # debug code
        # print("\n".join([",".join([(" " if len(str(i)) < 2 else "") + str(i) for i in row]) for row in mat]))
        return mat

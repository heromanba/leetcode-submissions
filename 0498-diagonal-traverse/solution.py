class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        # (0,0) -> (1,0) (0,1) -> (2,0) (1,1) (0,2) -> (2,1) (1,2) -> (2,2)
        # 0 -> 1 -> 2 -> 3 -> 4
        results = []
        for i in range(len(mat)+len(mat[0])-1):
            # i - len(mat[0]) + 1 <= j
            # 0 <= j
            lower_bound = max(0, i-len(mat[0])+1)
            # j <= len(mat) - 1
            # j <= i
            upper_bound = min(len(mat)-1, i)
            if i % 2 == 0:
                for j in range(upper_bound, lower_bound-1,-1):
                    results.append(mat[j][i-j])
            else:
                for j in range(lower_bound, upper_bound+1):
                    results.append(mat[j][i-j])
        return results


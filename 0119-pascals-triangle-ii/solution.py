class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(1, rowIndex+1+1):
            curr = i * [0]
            curr[0] = curr[-1] = 1
            if i > 2:
                for j in range(2, i):
                    curr[j-1] = result[-1][j-1] + result[-1][j-2]
            result.append(curr)
        return result[rowIndex]


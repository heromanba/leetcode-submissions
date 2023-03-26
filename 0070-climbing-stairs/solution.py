class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        table = [1, 2] + [None] * (n - 2)
        for i in range(2, len(table)):
            table[i] = table[i-1] + table[i-2]
        return table[-1]
    

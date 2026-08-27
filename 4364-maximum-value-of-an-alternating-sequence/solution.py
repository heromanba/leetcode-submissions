class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        if n == 1:
            return s
        if n % 2 == 1:
            return s + m*(n-1)//2-(n-2)//2
        else:
            return s + m*n//2-(n-1)//2

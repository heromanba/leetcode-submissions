class Solution:
    def minOperations(self, n: int) -> int:
        # find mid
        if n % 2 == 0:
            mid = ( (2*(n//2-1) + 1) + (2*(n//2) + 1) ) // 2
        else:
            mid = (2*(n//2) + 1)
        minOps = 0
        for i in range(n//2):
            minOps += abs( (2*i+1) - mid )
        return minOps


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        sum_v = 0
        piles = sorted(piles, reverse=True)
        for i in range(1, n+1):
            if 2*i-1 < len(piles):
                sum_v += piles[2*i-1]
        return sum_v

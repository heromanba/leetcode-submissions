class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        maxList = [None] * len(prices)
        # find the max of suffix
        for i in range(1, len(prices)+1):
            if i == 1:
                maxList[-1] = prices[-1]
            else:
                maxList[-i] = max(prices[-i], maxList[-i+1])
        ret = 0
        for i in range(len(prices)):
            if maxList[i] - prices[i] > ret:
                ret = maxList[i] - prices[i]
        return ret


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix_min_list = [None] * len(prices)
        postfix_max_list = [None] * len(prices)
        for i in range(len(prices)):
            if i == 0:
                prefix_min_list[i] = prices[i]
            else:
                prefix_min_list[i] = min(prefix_min_list[i-1], prices[i])
        for i in range(len(prices)-1, -1, -1):
            if i == len(prices)-1:
                postfix_max_list[i] = prices[i]
            else:
                postfix_max_list[i] = max(postfix_max_list[i+1], prices[i])
        max_delta = -1
        for i in range(len(prices)):
            max_delta = max(max_delta, postfix_max_list[i]-prefix_min_list[i])
        return max_delta


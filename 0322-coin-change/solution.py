class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for c in coins:
            for amt in range(c, amount+1):
                dp[amt] = min(dp[amt], dp[amt-c]+1)
        return -1 if dp[-1] == float('inf') else dp[-1]

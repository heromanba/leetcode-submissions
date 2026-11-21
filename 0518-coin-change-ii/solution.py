class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for c in coins:
            for amt in range(c, amount+1):
                dp[amt] += dp[amt-c]
        return dp[-1]

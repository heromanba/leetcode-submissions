class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        tot_sum = sum(nums)
        if tot_sum % 2 != 0:
            return False
        target_sum = tot_sum // 2
        dp = [
            [False for _ in range(target_sum+1)]
            for _ in range(len(nums)+1)
        ]
        dp[0][0] = True
        for i in range(1, len(nums)+1):
            n = nums[i-1]
            for s in range(1, target_sum+1):
                dp[i][s] = dp[i-1][s] or ( n <= s and dp[i-1][s-n] )
        return dp[len(nums)][target_sum]

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        dp = [ None for _ in range(len(nums)) ]
        dp[-1] = 0
        for i in range(len(nums)-2, -1, -1):
            if len(nums) - 1 - i > nums[i]:
                reachable_nodes = [dp[j] for j in range(i+1, i+nums[i]+1)]
                if reachable_nodes:
                    dp[i] = min(reachable_nodes) + 1
                else:
                    dp[i] = float('inf')
            else:
                dp[i] = 1
        return dp[0]

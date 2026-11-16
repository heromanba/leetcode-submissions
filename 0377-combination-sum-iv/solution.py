class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        
        dp = dict()
        dp[0] = 1

        def dfs(nums, target):
            if target in dp:
                return dp[target]
            result = 0
            for n in nums:
                if target - n >= 0:
                    result += dfs(nums, target-n)
            dp[target] = result
            return result
        
        dfs(nums, target)
        return dp[target] if target in dp else 0


class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        prefix_max = [0] * len(nums)
        max_sum = 0
        for i in range(len(nums)):
            if i == 0:
                prefix_max[i] = nums[i]
            else:
                prefix_max[i] = max(nums[i], prefix_max[i-1])
            if i >= k:
                max_sum = max(nums[i]+prefix_max[i-k], max_sum)
        return max_sum

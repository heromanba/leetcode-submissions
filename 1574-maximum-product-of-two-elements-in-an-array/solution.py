class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return nums
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        return (nums[-2] - 1) * (nums[-1] - 1)

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        previous_min_prod = None
        previous_max_prod = None
        max_sub = None
        for i in range(len(nums)):
            if i == 0:
                previous_min_prod = nums[0]
                previous_max_prod = nums[0]
                max_sub = nums[0]
            else:
                n = nums[i]
                new_min_prod = min(previous_min_prod*n, previous_max_prod*n, n)
                new_max_prod = max(previous_min_prod*n, previous_max_prod*n, n)
                previous_min_prod = new_min_prod
                previous_max_prod = new_max_prod
                max_sub = max(max_sub, new_max_prod)
        return max_sub

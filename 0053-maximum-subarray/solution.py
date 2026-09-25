class Solution:
    def maxSubArray(self, nums):
        max_sub = None
        previous_sum = None
        for n in nums:
            if previous_sum is None:
                previous_sum = n
                max_sub = n
            else:
                previous_sum = max(previous_sum+n, n)
                max_sub = max(max_sub, previous_sum)
        return max_sub

class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        tot_sum = sum(nums)

        prev_min = None
        prev_len = None
        min_sub = None
        for n in nums:
            if prev_min is None:
                prev_min = n
                min_sub = n
                prev_len = 1
            else:
                if prev_min + n >= n:
                    prev_min = n
                    prev_len = 1
                else:
                    prev_min = prev_min+n
                    prev_len += 1
                min_sub = min(min_sub, prev_min)
        if prev_len == len(nums):
            min_sub = tot_sum - max(nums)

        prev_max = None
        max_sub = None
        for n in nums:
            if prev_max is None:
                prev_max = n
                max_sub = n
            else:
                prev_max = max(prev_max+n, n)
                max_sub = max(max_sub, prev_max)
        
        return max(max_sub, tot_sum-min_sub)


class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        prev_min_sub = None
        prev_max_sub = None
        max_sub = None
        min_sub = None
        for n in nums:
            if prev_min_sub is None:
                prev_min_sub = n
                prev_max_sub = n
                max_sub = n
                min_sub = n
            else:
                new_min_sub = min(prev_min_sub+n, prev_max_sub+n, n)
                new_max_sub = max(prev_min_sub+n, prev_max_sub+n, n)
                prev_min_sub = new_min_sub
                prev_max_sub = new_max_sub
                max_sub = max(prev_max_sub, max_sub)
                min_sub = min(prev_min_sub, min_sub)
        return max(abs(max_sub), abs(min_sub), 0)

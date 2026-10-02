class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefix = [None] * len(nums)
        suffix = [None] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                prefix[0] = nums[0]
                suffix[-1] = nums[-1]
            else:
                prefix[i] = max(prefix[i-1], nums[i])
                suffix[-i-1] = min(suffix[-i], nums[-i-1])
        for i in range(len(nums)):
            if prefix[i] - suffix[i] <= k:
                return i
        return -1

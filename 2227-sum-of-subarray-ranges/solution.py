class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        sub_min = nums[:]
        sub_max = nums[:]
        result = 0
        for offset in range(len(nums)):
            for i in range(len(nums)-offset):
                end = i + offset # inclusive
                sub_min[i] = min(sub_min[i], nums[end])
                sub_max[i] = max(sub_max[i], nums[end])
                result += (sub_max[i]-sub_min[i])
        return result


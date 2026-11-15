class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i in range(len(nums)-1, 1, -1):
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                nums[i] = None
        start = None
        for end in range(len(nums)):
            if start is None and nums[end] is None:
                start = end
            if start is not None and nums[end] is not None:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
        return start if start is not None else len(nums)

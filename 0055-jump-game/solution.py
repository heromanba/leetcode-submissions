class Solution:
    def canJump(self, nums: list[int]) -> bool:
        start = 0
        end = 0
        while start <= end:
            end = max(end, start + nums[start])
            start += 1
            if end >= len(nums)-1:
                return True
        return False

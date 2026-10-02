class Solution:
    def minOperations(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0
        prev_x = None
        for i in range(len(nums)):
            if i == 0:
                prev_x = 0
            else:
                nums[i] += prev_x
                if nums[i-1] > nums[i]:
                    prev_x += (nums[i-1]-nums[i])
                    nums[i] = nums[i-1]
        return prev_x
                    


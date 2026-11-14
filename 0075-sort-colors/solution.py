class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lt = -1
        mid = 0
        gt = len(nums)
        while True:
            while mid < len(nums) and nums[mid] == 1:
                mid += 1
            if mid >= gt:
                break
            # print(lt, mid, gt, nums)
            if nums[mid] == 0:
                lt += 1
                nums[lt], nums[mid] = nums[mid], nums[lt]
                mid += 1
            else:
                gt -= 1
                nums[gt], nums[mid] = nums[mid], nums[gt]

                

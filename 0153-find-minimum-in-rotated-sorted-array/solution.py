class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:    # there must be rotation in mid ~ right
                left = mid + 1
            else:                          # there may or may not be rotation in left ~ mid.
                right = mid
        return nums[left]
                
            

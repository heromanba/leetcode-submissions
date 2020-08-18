class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid1 = (left + right) // 2
            mid2 = mid1 + 1
            if nums[mid1] < nums[mid2]:    # peak in right of mid1
                left = mid1 + 1
            else:                          # peak in left of mid1 (might be mid1)
                right = mid1
        return left

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ret = [-1, -1]
        if len(nums) < 1:
            return ret
        
        i = 0
        j = len(nums) - 1
        
        while i < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        
        if nums[i] != target:
            return ret
        else:
            ret[0] = i
        
        j = len(nums) - 1
        while (i < j):
            mid = (i + j) // 2 + 1
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid
        ret[1] = j
        return ret
        

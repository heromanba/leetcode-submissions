class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if target == nums[mid]:
                return mid
            
            if nums[left] <= nums[mid]:    # rotation pivot in mid ~ right
                # print("mid ~ right", left, mid, right)
                if nums[left] <= target < nums[mid]:
                    # make sure right part can be safely dropped.
                    right = mid -1 
                else:
                    left = mid + 1
            else:    # rotation pivot in left ~ mid
                # print("left ~ mid", left, mid, right)
                if nums[mid] < target <= nums[right]:
                    # make sure left part can be safely dropped.
                    left = mid + 1
                else:
                    right = mid - 1
        print(left, right)
        return -1

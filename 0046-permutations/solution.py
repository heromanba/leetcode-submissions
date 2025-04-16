class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(start):
            if start == len(nums):
                res.append(nums.copy())
                return
            for i in range(start, len(nums)):
                # Swap elements at indices 'start' and 'i'
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse for the next position
                backtrack(start + 1)
                # Undo the swap to backtrack
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return res

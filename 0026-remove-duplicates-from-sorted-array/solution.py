class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        cur = None
        for n in nums:
            if n != cur:
                nums[k] = n
                k += 1
                cur = n
        return k



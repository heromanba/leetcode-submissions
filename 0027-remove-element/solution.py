class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = 0
        for i in range(len(nums)):
            if nums[i] == val:
                for j in range(i, len(nums)):
                    if nums[j] != val:
                        nums[i] = nums[j]
                        nums[j] = val
                        break
        for i in range(len(nums)):
            if nums[i] == val:
                n += 1
        return len(nums) - n


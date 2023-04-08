class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            ret.append(nums[nums[i]])
        return ret

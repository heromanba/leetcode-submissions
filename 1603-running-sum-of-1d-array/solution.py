class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        running_sum = 0
        for i in nums:
            running_sum += i
            res.append(running_sum)
        return res

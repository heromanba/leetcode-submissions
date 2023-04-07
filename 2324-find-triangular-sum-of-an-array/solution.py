class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        triSum = nums
        for i in range(len(nums)-1, 0, -1):
            newTriSum = [None] * i
            for i in range(i):
                newTriSum[i] = (triSum[i] + triSum[i+1]) % 10
            triSum = newTriSum
        return triSum[0]



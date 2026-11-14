import statistics

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        median = statistics.median(nums)
        result = 0
        for n in nums:
            result += abs(median - n)
        return int(result)

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        n = len(nums) // 2
        res = []
        for i in range(n):
            freq = nums[2 * i]
            val = nums[2 * i + 1]
            res.extend([val] * freq)
        return res

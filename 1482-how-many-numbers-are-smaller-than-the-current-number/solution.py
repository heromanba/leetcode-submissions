class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = [0] * 101
        for i in nums:
            l[i] += 1
        print(l)
        res = []
        for i in nums:
            res.append(sum(l[:i]))
        return res

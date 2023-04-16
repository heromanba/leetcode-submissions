class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ret = []
        for n in nums:
            for d in str(n):
                ret.append(int(d))
        return ret

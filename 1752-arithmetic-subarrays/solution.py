class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ret = []
        for start, end in zip(l, r):
            range_v = sorted(nums[start:end+1])
            diff = range_v[1] - range_v[0]
            is_arith = True
            for i in range(len(range_v)-1):
                if range_v[i+1] - range_v[i] != diff:
                    is_arith = False
                    break
            ret.append(is_arith)
        return ret


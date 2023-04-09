class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        for i in range(1, len(nums)):
            left_sum.append(sum(nums[:i]))
        right_sum = []
        for i in range(len(nums)-1, 0, -1):
            right_sum.insert(0, sum(nums[i:]))
        right_sum.append(0)
        ret = []
        for l, r in zip(left_sum, right_sum):
            ret.append(abs(l - r))
        print(left_sum, right_sum)
        return ret

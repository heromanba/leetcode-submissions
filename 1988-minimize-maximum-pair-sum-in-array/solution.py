class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        ret = []
        max_sum = float('-inf')
        for i in range(len(new_nums)//2):
            sum_v = new_nums[i] + new_nums[-i-1]
            if sum_v > max_sum:
                max_sum = sum_v
        return max_sum


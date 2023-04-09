class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum = sum(nums)
        dig_sum = 0
        for n in nums:
            for d in str(n):
                dig_sum += int(d)
        return abs(ele_sum - dig_sum)

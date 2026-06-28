class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        ret = 0
        x_str = str(x)
        pre_sum = [0]*(len(nums)+1)
        for i in range(0,len(nums)):
            pre_sum[i+1]=pre_sum[i]+nums[i]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                sum_str = str(pre_sum[j]-pre_sum[i])
                left_most = sum_str[0]
                right_most = sum_str[-1]
                if left_most==x_str and right_most==x_str:
                    ret += 1
        return ret

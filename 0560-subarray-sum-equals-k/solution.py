class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]*len(nums)
        seen = dict()
        result = 0
        for i in range(len(nums)):
            if i == 0:
                prefix_sum[0] = nums[0]
            else:
                prefix_sum[i] = prefix_sum[i-1] + nums[i]
            if prefix_sum[i]-nums[i] not in seen:
                seen[prefix_sum[i]-nums[i]] = 1
            else:
                seen[prefix_sum[i]-nums[i]] += 1
            if prefix_sum[i] - k in seen:
                result += seen[prefix_sum[i] - k]
        return result

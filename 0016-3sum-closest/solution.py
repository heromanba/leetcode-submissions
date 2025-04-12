class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) <= 0:
            return sum(nums)
        nums = sorted(nums)
        ret = None
        diff = float('inf')
        for i in range(0, len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                tmp_sum = nums[i] + nums[j] + nums[k]
                tmp_diff = abs(tmp_sum-target)
                if tmp_diff < diff:
                    diff = tmp_diff
                    ret = tmp_sum
                if tmp_sum > target:
                    k -= 1
                elif tmp_sum < target:
                    j += 1
                else:
                    break
        return ret
        

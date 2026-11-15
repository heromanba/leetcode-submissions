import bisect
class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        result = 0
        nums = sorted([n%d for n in nums])
        # print(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                target = (d-(nums[i]+nums[j])%d)%d
                idx_left = bisect.bisect_left(nums[j+1:], target)
                idx_right = bisect.bisect_right(nums[j+1:], target)
                # print(nums[i], nums[j], target, nums[j+1:], idx_left, idx_right)
                if idx_left<len(nums[j+1:]) and nums[j+1:][idx_left] == target:
                    result += (idx_right-idx_left)
        return result

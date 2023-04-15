class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[j] - nums[i]) == k:
                    cnt += 1
        return cnt

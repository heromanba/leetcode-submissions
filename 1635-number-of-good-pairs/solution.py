class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_good_pairs = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    num_good_pairs += 1
        return num_good_pairs

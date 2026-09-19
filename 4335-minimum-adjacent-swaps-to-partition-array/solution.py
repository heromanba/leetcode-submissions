class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        num_swaps = 0
        part_2_3_nums = []

        part_1_idx = []
        for i in range(len(nums)):
            if nums[i] < a:
                part_1_idx.append(i)
            else:
                part_2_3_nums.append(nums[i])
        for i in range(len(part_1_idx)):
            num_swaps = (num_swaps+(part_1_idx[i] - i))%(10**9+7)

        part_2_idx = []
        for i in range(len(part_2_3_nums)):
            if a <= part_2_3_nums[i] and part_2_3_nums[i] <= b:
                part_2_idx.append(i)
        for i in range(len(part_2_idx)):
            num_swaps = (num_swaps+(part_2_idx[i] - i))%(10**9+7)
        
        return num_swaps

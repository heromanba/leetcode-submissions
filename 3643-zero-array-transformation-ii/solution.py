class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        all_zero = True
        for n in nums:
            if n != 0:
                all_zero = False
        if all_zero:
            return 0
        low = 0
        high = len(queries)
        k=-1
        while low < high:
            mid = low + (high-low)//2
            if self.check_all_zero(queries, nums[:], mid):
                high = mid
            else:
                low = mid+1
        # print(low, self.check_all_zero(queries, nums[:], low))
        return low+1 if self.check_all_zero(queries, nums[:], low) else -1
    
    def check_all_zero(self, queries, nums, end_idx):
        ev = [0] * len(nums)
        for l, r, val in queries[:end_idx+1]:
            ev[l] -= val
            if r+1 < len(nums):
                ev[r+1] += val
        # print(ev, nums)
        prev = None
        for i in range(len(ev)):
            if i == 0:
                prev = ev[0]
            else:
                prev += ev[i]
            nums[i] += prev
            if nums[i] > 0:
                return False
        return True

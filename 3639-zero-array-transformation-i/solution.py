class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        ev = [0]*len(nums)
        for l, r in queries:
            ev[l] -= 1
            if r+1 < len(nums):
                ev[r+1] += 1
        prev = None
        # print(ev)
        for i in range(len(ev)):
            if i == 0:
                prev = ev[0]
            else:
                prev += ev[i]
            # print(i, prev, nums[i])
            if prev+nums[i] > 0:
                return False
        return True


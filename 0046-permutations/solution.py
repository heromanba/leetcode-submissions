class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        self.backtrack([], nums)
        return self.ret

    def backtrack(self, curr_list, nums):
        if not nums:
            self.ret.append(curr_list)
            return
        for i in range(len(nums)):
            tmp_list = curr_list[:]
            tmp_list.append(nums[i])
            self.backtrack(tmp_list, nums[:i]+nums[i+1:])

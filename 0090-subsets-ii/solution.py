class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums = sorted(nums)
        def backtracking(candidates, curr_ret, target_len):
            if target_len == 0:
                # base case
                if curr_ret not in ret:
                    ret.append(curr_ret)
                return
            for idx, i in enumerate(candidates):
                backtracking(candidates[idx+1:], curr_ret + [i], target_len-1)
            return
        for i in range(len(nums)+1):
            backtracking(nums, [], i)
        return ret

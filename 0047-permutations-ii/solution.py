class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []
        cand_indices = list(range(len(nums)))
        def backtrack(candidates, curr_ret, target_len):
            if target_len == 0:
                ret.append(curr_ret)
                return
            for c in candidates:
                new_curr = curr_ret + [c]
                new_cand = [cand for cand in candidates if cand not in new_curr]
                backtrack(new_cand, new_curr, target_len-1)
            return
        backtrack(cand_indices, [], len(cand_indices))
        ret_v = []
        for id_list in ret:
            curr_ret = [nums[i] for i in id_list]
            if curr_ret not in ret_v:
                ret_v.append(curr_ret)
        return ret_v


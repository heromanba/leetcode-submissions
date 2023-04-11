class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def backtrack(candidates, curr_ret, target_len):
            if target_len == 0:
                ret.append(curr_ret)
                return
            for c in candidates:
                new_curr = curr_ret + [c]
                new_cand = [c for c in candidates if c not in new_curr]
                backtrack(new_cand, new_curr, target_len-1)
            return
        backtrack(nums, [], len(nums))
        return ret

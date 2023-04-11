class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ret = []
        def backtrack(candidates, start, curr_ret, target_len):
            if target_len == 0:
                ret.append(curr_ret)
                return
            for idx in range(start, len(s)):
                c = candidates[idx]
                if c.isalpha():
                    backtrack(candidates, idx+1, curr_ret+c.lower(), target_len-1)
                    backtrack(candidates, idx+1, curr_ret+c.upper(), target_len-1)
                else:
                    backtrack(candidates, idx+1, curr_ret+c, target_len-1)
            return
        backtrack(s, 0, "", len(s))
        return ret
            


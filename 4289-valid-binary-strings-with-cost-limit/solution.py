class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        
        valid_strs = []
        def backtrack(curr_str, curr_cost, n, k):
            if curr_cost > k:
                return
            if len(curr_str) == n:
                valid_strs.append(curr_str)
                return
            backtrack(curr_str+'0', curr_cost, n, k)
            if len(curr_str) == 0 or curr_str[-1] != '1':
                backtrack(curr_str+'1', curr_cost+len(curr_str), n, k)
        backtrack('', 0, n, k)
        return valid_strs

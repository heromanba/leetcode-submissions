class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        def backtrack(results, current_string, open, close, max):
            if len(current_string) == 2 * max:
                results.append(current_string)
                return
            if open < max:
                backtrack(results, current_string + "(", open + 1, close, max)
            if close < open:
                backtrack(results, current_string + ")", open, close + 1, max)
        backtrack(results, "", 0, 0, n)
        return results

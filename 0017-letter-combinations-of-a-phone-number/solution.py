class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        results = []
        if len(digits) == 0:
            return results
        def backtrack(results, current_str, current_pos, digits):
            if current_pos == len(digits):
                results.append(current_str)
                return
            for c in mapping[digits[current_pos]]:
                backtrack(results, current_str + c, current_pos + 1, digits)
        backtrack(results, "", 0, digits)
        return results
        

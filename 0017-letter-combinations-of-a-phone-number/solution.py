class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        results = []
        
        mapping = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y', 'z'],
        }
        def backtrack(digits, start, candidate):
            if start == len(digits):
                results.append(candidate)
                return
            for letter in mapping[digits[start]]:
                backtrack(digits, start+1, candidate+letter)
        
        backtrack(digits, 0, '')
        return results

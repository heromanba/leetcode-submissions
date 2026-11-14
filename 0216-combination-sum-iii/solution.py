class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        
        results = []
        def backtrack(start, chosen, k, remaining):
            if remaining == 0 and len(chosen) == k:
                results.append(chosen[:])
                return
            if start > 9 or remaining < 0 or len(chosen) >= k:
                return
            chosen.append(start)
            backtrack(start+1, chosen, k, remaining-start)
            chosen.pop()
            backtrack(start+1, chosen, k, remaining)
            return
        backtrack(1, [], k, n)
        return results

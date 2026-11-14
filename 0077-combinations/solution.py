class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        
        results = []
        def backtrack(n, start, chosen, remaining):
            if remaining == 0:
                results.append(chosen[:])
                return
            if start > n:
                return
            chosen.append(start)
            backtrack(n, start+1, chosen, remaining-1)
            chosen.pop()
            backtrack(n, start+1, chosen, remaining)
        backtrack(n, 1, [], k)
        return results


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occur = dict()
        for idx, c in enumerate(s):
            last_occur[c] = idx
        results = []
        in_results = set()
        for idx, c in enumerate(s):
            if c in in_results:
                continue
            while results and c < results[-1] and last_occur[results[-1]] > idx:
                top = results.pop()
                in_results.remove(top)
            results.append(c)
            in_results.add(c)
        return ''.join(results)

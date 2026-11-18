class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        suffix = [0] * (len(s)+1)
        for i in range(len(s)-1, -1, -1):
            if s[i] == letter:
                suffix[i] = suffix[i+1] + 1
            else:
                suffix[i] = suffix[i+1]
        result = []
        rep = 0
        for idx, c in enumerate(s):
            while result and \
                result[-1] > c and \
                len(result)+len(s)-1-idx >= k:
                if result[-1] == letter:
                    if rep-1+suffix[idx] < repetition:
                        # not enough letter left cannot pop
                        break
                    else:
                        rep -= 1
                result.pop()
            if len(result) < k:
                result.append(c)
                if c == letter:
                    rep += 1
            else:
                if c == letter and rep+suffix[idx] == repetition:
                    # have to add letter to result
                    n = suffix[idx]
                    for i in range(len(result)-1, -1, -1):
                        if result[i] != letter and n > 0:
                            result[i] = None
                            n -= 1
                    new_result = []
                    for r in result:
                        if r is not None:
                            new_result.append(r)
                    for i in range(suffix[idx]):
                        new_result.append(c)
                    result = new_result
                    break
        return ''.join(result)


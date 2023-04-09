class Solution:
    def sortSentence(self, s: str) -> str:
        ret = sorted([c for c in s.split(" ")], key=lambda x:x[-1])
        ret = " ".join([c[:-1] for c in ret])
        return ret

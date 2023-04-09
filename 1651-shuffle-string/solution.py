class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ret = [None] * len(s)
        for i, c in zip(indices, s):
            ret[i] = c
        return "".join(ret)

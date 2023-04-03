class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1, m+1))
        ret = []
        for i in queries:
            idx = p.index(i)
            ret.append(idx)
            v = p.pop(idx)
            p.insert(0, v)
        return ret

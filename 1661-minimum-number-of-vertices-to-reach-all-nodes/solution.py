class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        v_in = { e[1] for e in edges }
        v_all = set(range(n))
        return v_all.difference(v_in)

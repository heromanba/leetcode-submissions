class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        common = set(edges[0])
        for i in range(1, len(edges)):
            common = common.intersection(edges[i])
        return list(common)[0]


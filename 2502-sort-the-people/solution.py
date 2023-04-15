class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ret = sorted([(i, n) for i, n in enumerate(names)], key=lambda x: heights[x[0]], reverse=True)
        return [i[1] for i in ret]

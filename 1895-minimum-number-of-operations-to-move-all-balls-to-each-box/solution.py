class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # get index of all 1s
        ones = []
        for i, v in enumerate(boxes):
            if v == "1":
                ones.append(i)
        ret = []
        for i, v in enumerate(boxes):
            ret.append(sum([abs(i-j) for j in ones]))
        return ret

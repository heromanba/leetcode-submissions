class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [i for i in nums if i > 0]
        negative = [i for i in nums if i < 0]
        ret = []
        for pos, neg in zip(positive, negative):
            ret.extend([pos, neg])
        # inplace ?
        return ret

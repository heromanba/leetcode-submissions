class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        intersect = set(nums1).intersection(nums2)
        if intersect:
            return min(intersect)
        return -1

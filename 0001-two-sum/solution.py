class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = {}
        for idx, n in enumerate(nums):
            if target - n in record:
                return [record[target - n], idx]
            else:
                record[n] = idx
        return []

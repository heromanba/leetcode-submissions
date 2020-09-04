class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # store counts in a bucket.
        counts = [0 for _ in range(101)]
        for i in nums:
            counts[i] += 1
        for i in range(1, 101):
            counts[i] += counts[i-1]
        res = []
        for i in nums:
            if i == 0:
                res.append(0)
            else:
                res.append(counts[i-1])
        return res

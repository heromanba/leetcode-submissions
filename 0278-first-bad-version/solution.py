# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # search space.
        left, right = 1, n
                
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):    # search left part (might be mid).
                right = mid
            else:                    # search right part.
                left = mid + 1
        return left

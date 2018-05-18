class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter = 0
        for stone in S:
            if stone in J:
                counter += 1
        return counter

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        selfDividingNums = []
        for i in range(left, right + 1):
            num = str(i)
            num_len = len(num)
            for j in num:
                if (int(j) != 0)  and (i % int(j) == 0):
                    num_len -= 1
            if num_len == 0:
                selfDividingNums.append(i)
        return selfDividingNums

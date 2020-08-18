# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            flag = guess(mid)
            if flag == 1:    # mid < target
                left = mid + 1
            elif flag == -1:    # mid > target
                right = mid - 1
            elif flag == 0:
                return mid
        return -1

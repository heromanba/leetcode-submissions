class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            mid_square = mid ** 2
            if mid_square == x:
                return mid
            elif mid_square < x:
                left = mid + 1
            elif mid_square > x:
                right = mid - 1

        # End Condition: left > right
        return left - 1

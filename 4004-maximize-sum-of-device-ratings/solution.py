class Solution:
    def maxRatings(self, units: List[List[int]]) -> int:
        min_first = None
        min_second = None
        sum_rating = 0
        units = [sorted(u) for u in units]
        for u in units:
            if len(u) > 1:
                if min_second is None or u[1] < min_second :
                    min_second = u[1]
                sum_rating += u[1]
            else:
                sum_rating += u[0]

            if min_first is None or u[0] < min_first:
                min_first = u[0]

        if min_second is None:
            return sum_rating
        else:
            return sum_rating - min_second + min_first

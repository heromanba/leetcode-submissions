class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        bigger = []
        equal = []
        for n in nums:
            if n < pivot:
                less.append(n)
            elif n == pivot:
                equal.append(n)
            else:
                bigger.append(n)
        return less + equal + bigger

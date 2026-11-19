class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        result = None
        lower = max(0, k-len(nums2))
        upper = min(k, len(nums1))+1
        for ptr1 in range(lower, upper):
            max_num1 = self._get_max_num(nums1, ptr1)
            max_num2 = self._get_max_num(nums2, k-ptr1)
            curr = self._merge_two_max(max_num1, max_num2)
            print(lower, upper, max_num1, max_num2, curr)
            if result is None or curr > result:
                result = curr
        return result
        
    def _merge_two_max(self, a, b):
        merged = []
        i = j = 0
        while i < len(a) or j < len(b):
            if a[i:] >= b[j:]:
                merged.append(a[i]); i += 1
            else:
                merged.append(b[j]); j += 1
        return merged
                
    def _get_max_num(self, nums, l):
        result = []
        for idx, n in enumerate(nums):
            while result and result[-1] < n and len(nums)-1-idx+len(result) >= l:
                result.pop()
            if len(result) < l:
                result.append(n)
        return result

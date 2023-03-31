class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:] = nums2[:]
            return
        if n == 0:
            return
        # move 0s to first part of nums1
        for i in range(1, m+1):
            nums1[-i] = nums1[-n-i]
        # nums1: [0,0,0,0,8,8,8]
        # nums2: [2,5,6,7]
        ptr_m, ptr_n = n, 0
        for i in range(m + n):
            if (ptr_n >= n) or ((ptr_m < m + n) and (nums1[ptr_m] <= nums2[ptr_n])):
                # when to use nums1
                nums1[i] = nums1[ptr_m]
                ptr_m += 1
            elif (ptr_m >= m + n) or ((ptr_n < n) and (nums2[ptr_n] < nums1[ptr_m])):
                # when to use nums2
                nums1[i] = nums2[ptr_n]
                ptr_n += 1
            else:
                raise
        




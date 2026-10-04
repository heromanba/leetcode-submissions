class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1_cnt = dict()
        max_nums1 = float('-inf')
        for n in nums1:
            if n not in nums1_cnt:
                nums1_cnt[n] = 1
            else:
                nums1_cnt[n] += 1
            max_nums1 = max(max_nums1, n)

        nums2_cnt = dict()
        for n in nums2:
            if n not in nums2_cnt:
                nums2_cnt[n] = 1
            else:
                nums2_cnt[n] += 1

        ans = 0
        for n, cnt in nums2_cnt.items():
            for multiple in range(n*k, max_nums1+1, n*k):
                if multiple in nums1_cnt:
                    ans += cnt*nums1_cnt[multiple]
        return ans


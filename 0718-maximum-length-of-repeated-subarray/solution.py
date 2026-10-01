class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        ans = 0
        low = 1
        high = len(nums1) + 1
        while low < high:
            mid = low + (high-low)//2
            has_repeated = self.check_repeated(nums1, nums2, mid)
            # print(mid, has_repeated)
            if has_repeated:
                low = mid + 1
                ans = mid
            else:
                high = mid
        return ans

    def check_repeated(self, nums1, nums2, target_len):
        base = 107
        modulus = pow(10, 9) + 3
        power1 = pow(base, target_len-1)

        hash_set1 = set()
        nums1_hash = 0
        for i in range(len(nums1)-target_len+1):
            if i == 0:
                for j in range(target_len):
                    nums1_hash = (nums1_hash*base + nums1[j]) % modulus
            else:
                nums1_hash = (nums1_hash - nums1[i-1]*power1) % modulus
                nums1_hash = (nums1_hash*base + nums1[i+target_len-1]) % modulus
            hash_set1.add(nums1_hash)

        nums2_hash = 0
        for i in range(len(nums2)-target_len+1):
            if i == 0:
                for j in range(target_len):
                    nums2_hash = (nums2_hash*base + nums2[j]) % modulus
            else:
                nums2_hash = (nums2_hash - nums2[i-1]*power1) % modulus
                nums2_hash = (nums2_hash*base + nums2[i+target_len-1]) % modulus
            if nums2_hash in hash_set1:
                return True
        return False

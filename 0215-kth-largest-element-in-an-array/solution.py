class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest_nums = []
        for n in nums:
            if len(k_largest_nums) < k:
                k_largest_nums.append(n)
                k_largest_nums = self.putMinAtStart(k_largest_nums)
            else:
                min_k_largest = k_largest_nums[0]
                if n > min_k_largest:
                    k_largest_nums[0] = n
                    k_largest_nums = self.putMinAtStart(k_largest_nums)
        return k_largest_nums[0]
    
    def putMinAtStart(self, l: List[int]) -> List[int]:
        min_n = 10 ** 4 + 1
        min_idx = None
        for idx, i in enumerate(l):
            if i < min_n:
                min_n = i
                min_idx = idx
        n_start = l[0]
        l[0] = min_n
        l[min_idx] = n_start
        return l

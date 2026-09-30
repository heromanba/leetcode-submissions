class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        low = 1
        high = len(nums)+1
        
        ans = None

        base = 10**5+3
        modulus = 10**9+7
        while low < high:
            mid = low + (high-low)//2
            unique = set()
            non_unique = set()

            subarray = 0
            pow1 = pow(base, mid - 1, modulus)
            for i in range(0, len(nums)-mid+1):
                if i == 0:
                    for n in nums[i:i+mid]:
                        subarray = (subarray*base + n) % modulus
                else:
                    subarray = subarray - nums[i-1]*(pow1)
                    subarray = (subarray*base + nums[i+mid-1]) % modulus
                if subarray in non_unique:
                    continue
                elif subarray in unique:
                    unique.remove(subarray)
                    non_unique.add(subarray)
                else:
                    unique.add(subarray)
            if len(unique) > 0:
                high = mid
                ans = mid
            else:
                low = mid+1
        return ans



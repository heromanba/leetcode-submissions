class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        asc_sum = 0
        dsc_sum = 0
        for i in range(len(nums)):
            if i == 0:
                asc_sum += nums[i]
            else:
                if nums[i] > nums[i-1]:
                    asc_sum += nums[i]
                else:
                    if nums[i-1] > nums[i-2]:
                        dsc_sum += nums[i-1]
                    dsc_sum += nums[i]
        if asc_sum > dsc_sum:
            return 0
        elif asc_sum < dsc_sum:
            return 1
        else:
            return -1        

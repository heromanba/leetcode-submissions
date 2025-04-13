class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        nums.sort()

        ret = set()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                m, n = j+1, len(nums)-1
                while m < n:
                    tmp = nums[i] + nums[j] + nums[m] + nums[n]
                    if tmp == target:
                        if (nums[i], nums[j], nums[m], nums[n]) not in ret:
                            ret.add((nums[i], nums[j], nums[m], nums[n]))
                        m += 1
                    elif tmp < target:
                        m += 1
                    else:
                        n -= 1
        return [list(s) for s in ret]

class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        prefix_even = [0]*len(nums) + [0]
        prefix_odd = [0]*len(nums) + [0]
        for i in range(len(nums)):
            if nums[i]%2==0:
                prefix_even[i] = prefix_even[i-1] + 1
                prefix_odd[i] = prefix_odd[i-1]
            else:
                prefix_even[i] = prefix_even[i-1]
                prefix_odd[i] = prefix_odd[i-1] + 1
        print(prefix_even)
        num_valid = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                x = prefix_even[j]-prefix_even[i]
                y = prefix_odd[j]-prefix_odd[i]
                if nums[i]%2==0:
                    x+=1
                else:
                    y+=1
                if y > 0 and x/y<=a/b:
                    num_valid += 1

        return num_valid


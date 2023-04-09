class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum_v = 0
        for i in range(1, len(arr)+1):
            if i % 2 != 0:
                for j in range(len(arr)-i+1):
                    sum_v += sum(arr[j:j+i])
        return sum_v


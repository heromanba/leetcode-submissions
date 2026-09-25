class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        prefix_subsum = [None] * len(arr)
        prefix_sublen = [None] * len(arr)
        suffix_subsum = [None] * len(arr)
        suffix_sublen = [None] * len(arr)
        for i in range(len(arr)):
            if i == 0:
                prefix_subsum[0] = arr[0]
                prefix_sublen[0] = 1
            else:
                if prefix_subsum[i-1]+arr[i] >= arr[i]:
                    prefix_sublen[i] = prefix_sublen[i-1] + 1
                    prefix_subsum[i] = prefix_subsum[i-1]+arr[i]
                else:
                    prefix_sublen[i] = 1
                    prefix_subsum[i] = arr[i]

        for i in range(len(arr)-1, -1, -1):
            if i == len(arr)-1:
                suffix_subsum[len(arr)-1] = arr[-1]
                suffix_sublen[len(arr)-1] = 1
            else:
                if suffix_subsum[i+1]+arr[i] >= arr[i]:
                    suffix_subsum[i] = suffix_subsum[i+1]+arr[i]
                    suffix_sublen[i] = suffix_sublen[i+1] + 1
                else:
                    suffix_subsum[i] = arr[i]
                    suffix_sublen[i] = 1

        max_subsum = float('-inf')
        for i in range(len(arr)):
            if prefix_sublen[i] + suffix_sublen[i] - 2 > 0:
                max_subsum = max(max_subsum, prefix_subsum[i]+suffix_subsum[i]-2*arr[i], prefix_subsum[i]+suffix_subsum[i]-arr[i])
            else:
                max_subsum = max(max_subsum, arr[i])

        return max_subsum

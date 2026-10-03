class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        max_n = max(nums)
        cnt_map = dict()
        for n in nums:
            if n in cnt_map:
                cnt_map[n] += 1
            else:
                cnt_map[n] = 1
        replaced = {n: False for n in cnt_map}
        ans = 0
        for n in sorted(cnt_map):
            if replaced[n]:
                continue
            for multiple in range(n, max_n+1, n):
                if multiple in cnt_map and not replaced[multiple]:
                    ans += (n*cnt_map[multiple])
                    replaced[multiple] = True
        return ans


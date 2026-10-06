from collections import defaultdict
class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        dp = dict()
        for i in range(0, len(rods)+1):
            dp[i] = dict() # L-R: L
        dp[0][0] = 0
        for i in range(1, len(rods)+1):
            L = rods[i-1]
            for diff in dp[i-1]:
                # skip it
                dp[i][diff] = max(dp[i].get(diff, 0), dp[i-1].get(diff, 0))
                # put to the left
                dp[i][L+diff] = max(dp[i].get(L+diff, 0), dp[i-1].get(diff, 0)+L, dp[i-1].get(L+diff, 0))
                # put to the right
                # if i == 4 and diff-L == 1:
                #     print(dp[i-1].get(diff, 0), dp[i-1].get(diff-L, 0))
                dp[i][diff-L] = max(dp[i].get(diff-L, 0), dp[i-1].get(diff, 0), dp[i-1].get(diff-L, 0))
        # for row in dp:
        #     print(row, sorted(dp[row].items()))
        return dp[len(rods)][0]


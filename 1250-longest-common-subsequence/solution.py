class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [
            [float('-inf') for _ in range(len(text2)+1)]
            for _ in range(len(text1)+1)
        ]
        for i in range(len(text1)+1):
            dp[i][0] = 0
        for j in range(len(text2)+1):
            dp[0][j] = 0
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    # delete
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                    # insert
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
        # for row in dp:
        #     print(row)
        return dp[-1][-1]

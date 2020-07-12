class Solution {
public:
    int uniquePaths(int m, int n) {
        // Define dp array.
        int dp[m][n];
        
        // Set initial values.
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (i == 0)
                    dp[0][j] = 1;    // Upmost row.
                else if (j == 0)
                    dp[i][0] = 1;    // Leftmost column.
                else
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};

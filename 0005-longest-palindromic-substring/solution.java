class Solution {
    public String longestPalindrome(String s) {
        int max = -1;
        String longest = null;
        boolean[][] dp = new boolean[s.length()][s.length()];
        for(int i=s.length()-1; i>=0; i--) {
            for(int j=i; j<s.length(); j++) {
                dp[i][j] = s.charAt(i)==s.charAt(j)&&((j-i+1<3)||dp[i+1][j-1]);
                if((dp[i][j])&&(j-i+1>=max)) {
                    max=j-i+1;
                    longest=s.substring(i,j+1);
                }
            }
        }
        return longest;
    }
}

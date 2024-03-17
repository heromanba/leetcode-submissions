class Solution {
    public int[] countBits(int n) {
        int[] ret = new int[n+1];
        for (int i=0; i<=n; i++)
            ret[i]=numOfOnes(i);
        return ret;
    }
    
    private int numOfOnes(int n) {
        int ret = 0;
        while (n>0) {
            ret += n&1;
            n=n>>1;
        }
        return ret;
    }
}

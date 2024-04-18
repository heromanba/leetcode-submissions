class Solution {
    public int differenceOfSums(int n, int m) {
        int ret1 = 0;
        int ret2 = 0;
        for(int i=0; i<=n; i++) {
            if(i%m==0)
                ret2+=i;
            else
                ret1+=i;
        }
        return ret1-ret2;
    }
}

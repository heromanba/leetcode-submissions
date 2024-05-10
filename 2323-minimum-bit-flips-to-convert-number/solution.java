class Solution {
    public int minBitFlips(int start, int goal) {
        int tmp = start ^ goal;
        int ret = 0;
        while(tmp>0) {
            if(tmp%2==1)
                ret++;
            tmp=tmp>>1;
        }
        return ret;
    }
}

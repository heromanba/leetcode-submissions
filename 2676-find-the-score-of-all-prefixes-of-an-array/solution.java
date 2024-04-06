class Solution {
    public long[] findPrefixScore(int[] nums) {
        long[] ret = new long[nums.length];
        for(int i=0; i<nums.length; i++) {
            long max=nums[i];
            if(i==1) {
                max=Math.max(ret[i-1]-nums[i-1], nums[i]);
            } else if (i>1) {
                max=Math.max(ret[i-1]-nums[i-1]-ret[i-2], nums[i]);
            }
            ret[i]=nums[i]+max;
            if(i>=1) {
                ret[i]+=ret[i-1];
            }
        }
        // System.out.println(Arrays.toString(ret));
        return ret;
    }
}

class Solution {
    public int minOperations(int[] nums, int k) {
        int ret = 0;
        for(int n: nums)
            if(n<k)
                ret++;
        return ret;
    }
}

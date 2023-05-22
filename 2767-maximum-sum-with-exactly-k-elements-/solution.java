class Solution {
    public int maximizeSum(int[] nums, int k) {
        int[] tmp = new int[k];
        int max = Arrays.stream(nums).max().getAsInt();
        tmp[0] = max;
        for(int i=1; i<k; i++) {
            tmp[i] = tmp[i-1]+1;
        }
        int ret = Arrays.stream(tmp).sum();
        return ret;
    }
}

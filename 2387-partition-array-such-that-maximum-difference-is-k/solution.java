class Solution {
    public int partitionArray(int[] nums, int k) {
        if (nums.length==1)
            return 1;
        Arrays.sort(nums);
        
        int start = nums[0];
        int ret = 1;
        for (int i=1; i<nums.length; i++) {
            if (nums[i]-start>k) {
                ret += 1;
                start = nums[i];
            }
        }
        return ret;
    }
}

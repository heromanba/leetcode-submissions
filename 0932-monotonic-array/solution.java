class Solution {
    public boolean isMonotonic(int[] nums) {
        if(nums.length<=1)
            return true;
        boolean ascending = true;
        for(int i=0; i<nums.length-1; i++) {
            if (nums[i]>nums[i+1])
                ascending=false;
        }
        for(int i=0; i<nums.length-1; i++) {
            if(ascending&&((nums[i]>nums[i+1])))
                return false;
            else if(!ascending&&(nums[i]<nums[i+1]))
                return false;
        }
        return true;
    }
}

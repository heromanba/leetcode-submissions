class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> ret = new ArrayList<>();
        for(int i=0;i<nums.length;i++) {
            if((1<=nums[i])&&(nums[i]<=nums.length)) {
                while((nums[i]!=(i+1))&&(nums[i]!=nums[nums[i]-1])) {
                    int tmp = nums[nums[i]-1];
                    nums[nums[i]-1]=nums[i];
                    nums[i]=tmp;
                }
            }
        }
        for(int i=0; i<nums.length; i++){
            if(nums[i]!=i+1)
                ret.add(i+1);
        }
        return ret;
    }
}

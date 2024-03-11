class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        for (int i=0; i<nums.length; i++) {
            while ((nums[i]-1!=i)&&(nums[i]!=nums[nums[i]-1])) {
                // put nums[i] to the right position
                int temp = nums[nums[i]-1];
                nums[nums[i]-1] = nums[i];
                nums[i]=temp;
            }
        }
        List<Integer> ret = new ArrayList<>();
        for (int i=0; i<nums.length; i++) {
            if (nums[i]-1!=i)
                ret.add(nums[i]);
        }
        return ret;
    }
}

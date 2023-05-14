class Solution {
    public int maxOr = 0;
    public int numEq = 0;

    public void backtrack(int[] nums, int i, int currOr) {
        if(i==nums.length) {
            if(currOr == maxOr) {
                numEq++;
            }
            return;
        }
        backtrack(nums, i+1, currOr|nums[i]);
        backtrack(nums, i+1, currOr);
    }
    public int countMaxOrSubsets(int[] nums) {
        for(int i=0; i<nums.length; i++) {
            maxOr |= nums[i];
        }
        backtrack(nums, 0, 0);
        return numEq;
    }
}

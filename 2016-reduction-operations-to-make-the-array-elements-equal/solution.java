class Solution {
    public int reductionOperations(int[] nums) {
        Arrays.sort(nums);
        int min = nums[0];
        int tmp = 0;
        int total = 0;
        for (int i=1; i<nums.length; i++) {
            if (nums[i]!=nums[i-1])
                tmp += 1;
            if (nums[i]>min)
                total += tmp;
        }
        return total;
    }
}

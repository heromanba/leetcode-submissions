class Solution {
    public int matrixSum(int[][] nums) {
        for(int i=0; i<nums.length; i++) {
            Arrays.sort(nums[i]);
        }
        int ret = 0;
        for(int j=0; j<nums[0].length; j++) {
            int max = -1;
            for(int i=0; i<nums.length; i++)
                if(nums[i][j]>max)
                    max=nums[i][j];
            ret+=max;
        }
        return ret;
    }
}

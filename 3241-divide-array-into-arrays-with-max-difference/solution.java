class Solution {
    public int[][] divideArray(int[] nums, int k) {
        int[][] ret = new int[nums.length/3][3];
        Arrays.sort(nums);
        for (int i=0; i<ret.length; i++) {
            if (nums[i*3+2]-nums[i*3]>k) {
                int[][] empty = new int[0][0];
                return empty;
            }
            int[] tmp=new int[3];
            for (int j=0; j<3; j++) {
                tmp[j]=nums[i*3+j];
            }
            ret[i]=tmp;
        }
        return ret;
    }
}

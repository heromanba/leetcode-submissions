class Solution {
    public void moveZeroes(int[] nums) {
        int end = nums.length-1;
        for(int i=0; i<nums.length; i++) {
            while ((nums[i]==0)&&(i<end)){
                for (int j=i;j<end;j++)
                {
                    nums[j]=nums[j+1];
                }
                nums[end]=0;
                end -= 1;
            }
        }
        
    }
}

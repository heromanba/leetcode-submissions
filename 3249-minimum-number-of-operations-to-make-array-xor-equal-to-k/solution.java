class Solution {
    public int minOperations(int[] nums, int k) {
        int temp = 0;
        for (int i=0; i<nums.length; i++) {
            temp ^= nums[i];
        }
        temp ^= k;
        int cnt = 0;
        while (temp > 0) {
            if (temp%2==1) {
                cnt +=1;
            }
            temp /= 2;
        }
        return cnt;
    }
}

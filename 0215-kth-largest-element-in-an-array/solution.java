class Solution {
    public int findKthLargest(int[] nums, int k) {
        int l = 0, h = nums.length - 1;
        k = nums.length - k;
        while(true) {
            int p = part(nums, l, h);
            if (p == k) break;
            else if (p < k) {
                l = p + 1;
            } else {
                h = p - 1;
            }
        }
        
        return nums[k];
    }
    
    private int part(int[] nums, int l, int r) {
        swap(nums, (l + r) / 2, r);
        int p = r--;
        while(l <= r) {
            if (nums[l] >= nums[p]) {
                swap(nums, l, r--);
            } else {
                l++;
            }
        }
        
        swap(nums, l, p);
        return l;
    }
    
    private void swap (int[] nums, int left, int right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
    }
}

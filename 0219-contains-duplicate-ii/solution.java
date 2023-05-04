class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> mem = new HashMap<>();
        int minIndex = -1;
        for(int i=0; i<nums.length; i++) {
            if (mem.containsKey(nums[i])) {
                int lastIdx = mem.get(nums[i]);
                if (i - lastIdx <= k) {
                    return true;
                } 
            }
            mem.put(nums[i], i);
        }
        return false;
    }
}

class Solution {
    public int missingNumber(int[] nums) {
        
        Set<Integer> targetSet = new HashSet<>();
        for (int i: nums)
            targetSet.add(i);
        for (int i=1; i<nums.length+1; i++){
            if(!targetSet.contains(i))
                return i;
        }
        return 0;
    }
}

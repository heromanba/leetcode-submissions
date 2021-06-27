class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i : nums) {
            set.add(i);
        }
        int longest = 0;
        for (int i : nums) {
            if (!set.contains(i - 1)) {
                // i is left end;
                int j = i + 1;
                while (set.contains(j)) {
                    j++;
                }
                longest = Math.max(longest, j - i);
            }
        }
        return longest;
    }
}

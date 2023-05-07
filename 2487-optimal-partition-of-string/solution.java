class Solution {
    public int partitionString(String s) {
        int numParts = 0;
        int end = 0;
        Set<Character> seen = new HashSet<>();
        while(end < s.length()) {
            Character c = s.charAt(end);
            if (seen.contains(c)) {
                numParts += 1;
                seen.clear();
            }
            seen.add(c);
            end++;
        }
        if (!seen.isEmpty())
            numParts += 1;
        return numParts;
    }
}

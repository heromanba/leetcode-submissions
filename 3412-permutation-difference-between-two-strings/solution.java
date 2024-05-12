class Solution {
    public int findPermutationDifference(String s, String t) {
        Map<Character, Integer> tmp = new HashMap<>();
        for(int i=0; i<s.length(); i++) {
            tmp.put(s.charAt(i), i);
        }
        int ret = 0;
        for(int i=0; i<t.length(); i++) {
            ret += Math.abs(i-tmp.get(t.charAt(i)));
        }
        return ret;
    }
}

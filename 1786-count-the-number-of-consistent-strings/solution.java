class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        Set<Character> set = new HashSet<>();
        for(char c: allowed.toCharArray())
            set.add(c);
        int ret = 0;
        for(String word: words) {
            boolean tmp = true;
            for(char c: word.toCharArray()) {
                if(!set.contains(c)) {
                    tmp=false;
                    break;
                }
            }
            if(tmp)
                ret++;
        }
        return ret;
    }
}

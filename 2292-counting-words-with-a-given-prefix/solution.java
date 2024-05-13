class Solution {
    public int prefixCount(String[] words, String pref) {
        int ret = 0;
        for(String s: words)
            if(s.startsWith(pref))
                ret++;
        return ret;
    }
}

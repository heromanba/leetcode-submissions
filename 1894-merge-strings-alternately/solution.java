class Solution {
    public String mergeAlternately(String word1, String word2) {
        int minLen = Math.min(word1.length(), word2.length());
        String ret = "";
        for(int i=0; i<minLen; i++){
            ret += word1.charAt(i);
            ret += word2.charAt(i);
        }
        if (minLen >= word1.length())
            ret += word2.substring(minLen, word2.length());
        if (minLen >= word2.length())
            ret += word1.substring(minLen, word1.length());

        return ret;
    }
}

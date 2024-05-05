class Solution {
    public String reversePrefix(String word, char ch) {
        int idx = word.indexOf(ch);
        String prefix = new StringBuilder(word.substring(0, idx+1)).reverse().toString();
        return prefix + word.substring(idx+1);
    }
}

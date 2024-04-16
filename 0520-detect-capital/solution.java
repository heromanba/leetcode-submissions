class Solution {
    public boolean detectCapitalUse(String word) {
        if(word.equals(word.toUpperCase()))
            return true;
        if(word.equals(word.toLowerCase()))
            return true;
        if(Character.isUpperCase(word.charAt(0))) {
            if(word.substring(1,word.length()).toLowerCase().equals(word.substring(1,word.length())))
                return true;
        }
        return false;
    }
}

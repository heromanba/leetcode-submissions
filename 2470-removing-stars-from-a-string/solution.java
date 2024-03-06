class Solution {
    public String removeStars(String s) {
        int numStars = 0;
        StringBuilder ret = new StringBuilder();
        for (int i=s.length()-1; i>=0; i--) {
            if (s.charAt(i)=='*') 
                numStars += 1;
            else if (numStars > 0)
                numStars -= 1;
            else
                ret.append(s.charAt(i));
        }
        return ret.reverse().toString();
    }
}

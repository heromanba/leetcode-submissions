class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length()>t.length())
            return false;
        int prev=0;
        for(int i=0;i<s.length();i++) {
            for(int j=prev;j<t.length();j++){
                if(s.charAt(i)==t.charAt(j)) {
                    prev=j+1;
                    break;
                } else {
                    if(s.length()-i>t.length()-j-1)
                        return false;
                }
            }
        }
        return true;
    }
}

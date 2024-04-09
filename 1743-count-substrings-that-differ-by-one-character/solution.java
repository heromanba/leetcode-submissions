class Solution {
    public int countSubstrings(String s, String t) {
        int size=Math.min(s.length(),t.length());
        int ret=0;
        for(int i=1;i<=size;i++){
            for(int j=0;j<=s.length()-i;j++) {
                for(int k=0;k<=t.length()-i;k++) {
                    if(oneDiff(s, j, t, k, i))
                        ret+=1;
                }
            }
        }
        return ret;
    }
    
    private boolean oneDiff(String s1, int j, String s2, int k, int i) {
        int diff=0;
        for(int n=0;n<i;n++){
            if(s1.charAt(j+n)!=s2.charAt(k+n))
                diff++;
            if(diff>1)
                return false;
        }
        return diff==1;
    }
}

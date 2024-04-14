class Solution {
    private Map<String, Boolean> mem = new HashMap<>();
    
    public int countSubstrings(String s) {
        int ret = 0;
        for(int i=0; i<s.length(); i++) {
            for(int j=i+1; j<=s.length(); j++) {
                if(palindromic(s.substring(i, j)))
                    ret++;
            }
        }
        return ret;
    }
    
    private boolean palindromic(String s) {
        if(mem.containsKey(s))
            return mem.get(s);
        if(s.length()==1) {
            return true;
        }
        int half = s.length() / 2;
        for(int i=0; i<half; i++) {
            if(s.charAt(i)!=s.charAt(s.length()-i-1)) {
                mem.put(s, false);
                return false;
            }
        }
        mem.put(s, true);
        return true;
    }
}

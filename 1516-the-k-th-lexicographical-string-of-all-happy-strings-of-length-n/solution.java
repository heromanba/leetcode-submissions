class Solution {
    public String getHappyString(int n, int k) {
        int maxLen = 3 * (int) Math.pow(2, n-1);
        if (k>maxLen)
            return "";
        StringBuilder ret = new StringBuilder();
        for (int i=0; i<n; i++) {
            
            if (i==0) {
                if (k>2*(int) Math.pow(2, n-1)) {
                    k = k - 2*(int) Math.pow(2, n-1-i);
                    ret.append('c');
                }
                else if (k>1*(int) Math.pow(2, n-1)) {
                    k = k - (int) Math.pow(2, n-1-i);
                    ret.append('b');
                } else {
                    ret.append('a');
                }
            } else {
                String candidates = "abc";
                candidates = candidates.replace(ret.substring(ret.length()-1), "");
                if (k>(int) Math.pow(2, n-1-i)) {
                    k = k - (int) Math.pow(2, n-1-i);
                    ret.append(candidates.charAt(1));
                }
                else
                    ret.append(candidates.charAt(0));
            }
        }
        return ret.toString();
    }
}

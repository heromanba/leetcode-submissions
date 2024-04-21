class Solution {
    public int minInsertions(String s) {
        int i=0;
        int balance=0;
        int ret=0;
        while(i<s.length()) {
            if(s.charAt(i)=='(') {
                balance++;
            }
            else {
                if((i+1<s.length())&&(s.charAt(i+1)==')')) {
                    balance--;
                    i++;
                } else {
                    ret++;
                    balance--;
                }
            }
            if(balance==-1) {
                balance=0;
                ret++;
            }
            i++;
        }
        return ret+2*balance;
    }
}

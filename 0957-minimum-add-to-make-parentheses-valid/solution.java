class Solution {
    public int minAddToMakeValid(String s) {
        int ret = 0;
        int balance = 0;
        for(int i=0; i<s.length(); i++) {
            if(s.charAt(i)=='(')
                balance++;
            else
                balance--;
            if(balance==-1) {
                ret++;
                balance=0;
            }
        }
        ret += balance;
        return ret;
    }
}

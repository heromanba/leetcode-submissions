class Solution {
    public int minSwaps(String s) {
        char[] ss = s.toCharArray();
        int ret = 0;
        int balance = 0;
        int balanceFromLeft = 0;
        int j = ss.length-1;
        for(int i=0; i<ss.length; i++) {
            if(i==j)
                break;
            if(ss[i]=='[') {
                balance++;
            } else {
                balance--;
            }
            if(balance==-1) {
                while(j>i) {
                    if(ss[j]=='[') {
                        balanceFromLeft++;
                    } else {
                        balanceFromLeft--;
                    }
                    if(balanceFromLeft==1) {
                        swap(ss, i, j);
                        balanceFromLeft = 1;
                        balance=1;
                        ret++;
                        break;
                    }
                    j--;
                }
            }
        }
        return ret;
    }
    
    private void swap(char[] s, int i, int j) {
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }
}

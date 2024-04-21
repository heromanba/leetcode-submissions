class Solution {
    public String minRemoveToMakeValid(String s) {
        int balance = 0;
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<s.length(); i++) {
            if((s.charAt(i)!='(')&&(s.charAt(i)!=')')) {
                sb.append(s.charAt(i));
                continue;
            }
            if(s.charAt(i)=='(')
                balance++;
            else
                balance--;
            if(balance==-1) {
                balance=0;
            } else {
                sb.append(s.charAt(i));
            }
        }
        if(balance > 0) {
            for(int i=sb.length()-1; i>=0; i--) {
                if(balance==0)
                    break;
                if(sb.charAt(i)=='(') {
                    sb.deleteCharAt(i);
                    balance--;
                }
            }
        }
        return sb.toString();
    }
}

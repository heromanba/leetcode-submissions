class Solution {
    public String convertToBase7(int num) {
        if (num==0)
            return "0";
        StringBuilder sb = new StringBuilder();
        int tmp = Math.abs(num);
        while(tmp>0) {
            sb.append(tmp%7);
            tmp/=7;
        }
        if(num>0)
            return sb.reverse().toString();
        else
            return "-"+sb.reverse().toString();
    }
}

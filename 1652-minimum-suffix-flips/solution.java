class Solution {
    public int minFlips(String target) {
        int num = 0;
        for (int i=target.length()-1; i>0; i--) {
            if (target.charAt(i)!=target.charAt(i-1))
                num += 1;
        }
        if (target.charAt(0)=='1')
            num += 1;
        return num;
    }
}

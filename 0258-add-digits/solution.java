class Solution {
    public int addDigits(int num) {
        while (num > 9) {
            num = getDiditSum(num);
        }
        return num;
    }
    
    private int getDiditSum(int num) {
        int ret = 0;
        while (num > 0) {
            ret += num % 10;
            num /= 10;
        }
        return ret;
    }
}

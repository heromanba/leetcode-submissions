class Solution {
    public boolean isPowerOfFour(int n) {
        int p = 0;
        while (true) {
            if (Math.pow(4, p)==n)
                return true;
            if (Math.pow(4, p)>n)
                break;
            p+=1;
        }
        return false;
    }
}

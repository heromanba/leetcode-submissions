class Solution {
    public boolean isPowerOfThree(int n) {
        int p=0;
        while (true) {
            if (Math.pow(3,p)==n)
                return true;
            if (Math.pow(3,p)>n)
                return false;
            p+=1;
        }
    }
}

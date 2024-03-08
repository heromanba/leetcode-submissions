class Solution {
    public boolean isPowerOfTwo(int n) {
        int i = 0;
        long m = (long) n;
        while (true) {
            long pow = (long) Math.pow(2, i);
            if (pow > m)
                return false;
            if (pow == m)
                return true;
            i += 1;
        }
    }
}

class Solution {
    public int numberOfMatches(int n) {
        int numMatches = 0;
        while (n > 1) {
            if (n % 2 == 0) {
                numMatches += n / 2;
                n = n / 2;
            } else {
                numMatches += (n - 1) / 2;
                n = (n - 1) / 2 + 1;
            }
        }
        return numMatches;
    }
}

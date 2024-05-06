class Solution {
    public int pivotInteger(int n) {
        int lo = 1;
        int hi = n;
        int first = 0;
        int second = 0;
        while(lo<hi) {
            if(first>second) {
                second+=hi;
                hi--;
            } else {
                first+=lo;
                lo++;
            }
        }
        if(first==second)
            return lo;
        else
            return -1;
    }
}

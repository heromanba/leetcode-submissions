class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int max = -1;
        for (int c: costs) {
            if (c>max)
                max = c;
        }
        int[] countArr = new int[max];
        for (int c: costs) {
            countArr[c-1] += 1;
        }
        int ret = 0;
        for (int i=0; i<max; i++) {
            for (int j=0; j<countArr[i]; j++) {
                if (coins>=i+1) {
                    ret += 1;
                    coins -= (i+1);
                }
            }
        }
        return ret;
    }
}

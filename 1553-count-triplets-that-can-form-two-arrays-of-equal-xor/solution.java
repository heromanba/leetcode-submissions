class Solution {
    public int countTriplets(int[] arr) {
        int ret = 0;
        for (int i=0; i<arr.length-1; i++) {
            int xor = arr[i];
            for(int k=i+1; k<arr.length; k++) {
                xor ^= arr[k];
                if (xor==0) {
                    ret += (k-i);
                    // System.out.println("k: "+k+"i: "+i);
                }
            }
        }
        return ret;
    }
}

class Solution {
    public int[] memLeak(int memory1, int memory2) {
        int[] ret = new int[3];
        int i = 1;
        while(i<=Math.max(memory1, memory2)) {
            if(memory1>=memory2) {
                memory1 -= i;
            } else {
                memory2 -= i;
            }
            i += 1;
        }
        ret[0] = i;
        ret[1] = memory1;
        ret[2] = memory2;
        return ret;
    }
}

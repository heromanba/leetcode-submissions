class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        int[] ret = new int[A.length];
        Set<Integer> scannedA = new HashSet<>();
        Set<Integer> scannedB = new HashSet<>();
        for(int i=0; i<A.length; i++) {
            if (A[i] == B[i]) {
                if (i>0)
                    ret[i] = ret[i-1]+1;
                else
                    ret[i] = 1;
            } else {
                if (i>0)
                    ret[i] = ret[i-1];
                else
                    ret[i] = 0;
                if (scannedB.contains(A[i]))
                    ret[i]+=1;
                if (scannedA.contains(B[i]))
                    ret[i]+=1;
            }
            scannedA.add(A[i]);
            scannedB.add(B[i]);
        }
        return ret;
    }
}

class Solution {
    public int largestCombination(int[] candidates) {
        int maxCom = Integer.MIN_VALUE;
        int maxLen = Integer.MIN_VALUE;
        List<List<Integer>> reprs = new ArrayList<>();
        for(int i=0; i<candidates.length; i++) {
            List<Integer> repr = getBinReprLast(candidates[i]);
            reprs.add( repr );
            if(repr.size()>maxLen)
                maxLen = repr.size();
        }
        for(int i=0; i<maxLen; i++){
            int numOnes = 0;
            for(List<Integer> repr: reprs) {
                if(i<repr.size()) {
                    if(repr.get(i)==1) {
                        numOnes++;
                    }
                }
            }
            if(numOnes > maxCom)
                maxCom = numOnes;
        }
        return maxCom;
    }

    public List<Integer> getBinReprLast(int n) {
        // System.out.println(n);
        List<Integer> ret = new ArrayList<>();
        while (true) {
            ret.add(n%2);
            if(n==0)
                break;
            n=n/2;
        }
        // System.out.println(ret);
        return ret;        
    }
}

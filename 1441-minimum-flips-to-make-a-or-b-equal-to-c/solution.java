class Solution {
    public int minFlips(int a, int b, int c) {
        List<Integer> aBin = toBinRepr(a);
        List<Integer> bBin = toBinRepr(b);
        List<Integer> cBin = toBinRepr(c);
        int max = Collections.max(Arrays.asList(aBin.size(), bBin.size(), cBin.size()));
        int cnt=0;
        for (int i=0; i<max; i++) {
            int aBit=0;
            if (i<aBin.size())
                aBit=aBin.get(i);
            int bBit=0;
            if (i<bBin.size())
                bBit=bBin.get(i);
            int cBit=0;
            if (i<cBin.size())
                cBit=cBin.get(i);
            // System.out.println("a: "+aBit+"b: "+bBit+"c: "+cBit);
            if ((aBit|bBit)!=cBit) {
                if (cBit==1)
                    cnt+=1;
                else {
                    if (aBit==1)
                        cnt+=1;
                    if (bBit==1)
                        cnt+=1;
                }
            }
        }
        return cnt;
        
    }
    
    private List<Integer> toBinRepr(int n) {
        List<Integer> ret = new ArrayList<>();
        while (n>0) {
            ret.add(n%2);
            n/=2;
        }
        return ret;
    }
}

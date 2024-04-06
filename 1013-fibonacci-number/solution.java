class Solution {
    private int[] mem = null;
    
    public int fib(int n) {
        if(n==0)
            return 0;
        if(n==1)
            return 1;
        mem = new int[n+1];
        mem[0] = 0;
        mem[1] = 1;
        for(int i=2; i<=n; i++) {
            mem[i] = mem[i-1] + mem[i-2];
        }
        return mem[n];
    }
}

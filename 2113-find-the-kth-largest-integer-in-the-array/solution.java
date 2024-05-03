import java.math.BigInteger;
class Solution {
    private String[] heap;
    private int N=0;
    
    private void exch(int i, int j) {
        String tmp = heap[i];
        heap[i] = heap[j];
        heap[j] = tmp;
    }
    
    private void insert(String s) {
        heap[N++] = s;
        swim(N-1);
    }
    
    private void delMin() {
        heap[0] = heap[--N];
        heap[N]=null;
        sink(0);
    }
    
    private void swim(int i) {
        while(i>=0) {
            int parent = (i+1)/2-1;
            if((parent>=0)&&(!less(heap[parent], heap[i]))) {
                exch(parent, i);
                i = parent;
            } else
                break;
        }
    }
    
    private void sink(int i) {
        while(i<N) {
            int left = (i+1) * 2 - 1;
            int right = (i+1) * 2;
            int child;
            if((right<N)&&(less(heap[right], heap[left]))) {
                child=right;
            } else if (left<N)
                child=left;
            else
                break;
            if(!less(heap[i], heap[child])) {
                exch(i, child);
                i = child;
            } else 
                break;
        }
    }
    
    public String kthLargestNumber(String[] nums, int k) {
        heap = new String[k];
        
        for(String s: nums) {
            if(N<k)
                insert(s);
            else {
                if(!less(s, heap[0])) {
                    delMin();
                    // System.out.println(Arrays.asList(heap));
                    insert(s);
                }
            }
        }
        return heap[0];
    }
    
    private boolean less(String i, String j) {
        BigInteger ii = new BigInteger(i);
        BigInteger jj = new BigInteger(j);
        return ii.compareTo(jj) < 0;
    }
}

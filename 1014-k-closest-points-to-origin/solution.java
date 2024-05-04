class Solution {
    
    private int[][] heap;
    private int N;
    
    private void exch(int i, int j) {
        int[] tmp = heap[i];
        heap[i] = heap[j];
        heap[j] = tmp;
    }
    
    private boolean less(int[] a, int[] b) {
        Double distA = Math.pow(a[0], 2)+Math.pow(a[1], 2);
        Double distB = Math.pow(b[0], 2)+Math.pow(b[1], 2);
        return distA < distB;
    }
    
    private void insert(int[] a) {
        heap[N++] = a;
        swim(N-1);
    }
    
    private void delMax() {
        heap[0] = heap[--N];
        heap[N] = null;
        sink(0);
    }
    
    private void sink(int i) {
        while(i<N) {
            int left = (i+1)*2-1;
            int right = (i+1)*2;
            int child;
            if((right<N)&&(less(heap[left], heap[right])))
                child = right;
            else if (left<N)
                child = left;
            else 
                break;
            if(less(heap[i], heap[child])) {
                exch(i, child);
                i = child;
            } else
                break;
        }
    }
    
    private void swim(int i) {
        while(i>=0) {
            int parent = (i+1)/2-1;
            if((parent>=0)&&(less(heap[parent], heap[i]))) {
                exch(parent, i);
                i = parent;
            } else 
                break;
        }
    }
    public int[][] kClosest(int[][] points, int k) {
        heap = new int[k][2];
        for(int[] pt: points) {
            if(N<k)
                insert(pt);
            else{
                if(less(pt, heap[0])) {
                    delMax();
                    insert(pt);
                }
            }
        }
        return heap;
    }
}

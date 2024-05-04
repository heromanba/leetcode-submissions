class SeatManager {
    
    private int[] heap;
    private int N;
    
    private Set<Integer> reserved = new HashSet<>();
    
    private void exch(int i, int j) {
        int tmp = heap[i];
        heap[i] = heap[j];
        heap[j] = tmp;
    }
    
    private void insert(int i) {
        heap[N++] = i;
        swim(N-1);
    }
    
    private int delMin() {
        int ret = heap[0];
        heap[0] = heap[--N];
        sink(0);
        return ret;
    }
    
    private void swim(int child) {
        while(child>=0) {
            int parent = (child+1)/2-1;
            if((parent>=0)&&(heap[parent]>heap[child])) {
                exch(parent, child);
                child = parent;
            } else
                break;
        }
    }
    
    private void sink(int parent) {
        while(parent<N) {
            int left = (parent+1)*2-1;
            int right = (parent+1)*2;
            int child;
            if((right<N)&&(heap[right]<heap[left]))
                child = right;
            else if(left<N)
                child = left;
            else 
                break;
            if(heap[parent]>heap[child]) {
                exch(parent, child);
                parent = child;
            } else
                break;
        }
    }
    
    public SeatManager(int n) {
        heap = new int[n];
        for(int i=1; i<=n; i++) 
            heap[i-1]=i;
        N=n;
    }
    
    public int reserve() {
        int ret = delMin();
        reserved.add(ret);
        return ret;
    }
    
    public void unreserve(int seatNumber) {
        reserved.remove(seatNumber);
        insert(seatNumber);
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */

class Solution {
    
    private Integer[] heap;
    private int N = 0;
    
    private void exch(int i, int j) {
        int tmp = heap[i];
        heap[i] = heap[j];
        heap[j] = tmp;
    }
    
    private void delMin() {
        heap[0] = heap[--N];
        heap[N] = null;
        sink(0);
    }
    
    private void sink(int i) {
        while(i < N) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int child;
            if ((right <= N-1) && (heap[right] < heap[left]))
                child = right;
            else if (left <= N-1)
                child = left;
            else
                break;
            if(heap[child] < heap[i]) {
                exch(i, child);
                i = child;
            } else
                break;
        }
    }
    
    private void swim(int i) {
        while(i >= 0) {
            int parent = (i+1)/2-1;
            if((parent>=0)&&(heap[parent] > heap[i])) {
                exch(i, parent);
                i = parent;
            }
            else
                break;
        }
    }
    
    private void insert(int i) {
        heap[N++] = i;
        swim(N-1);
    }
    
    public int findKthLargest(int[] nums, int k) {
        heap = new Integer[k];
        for(int i: nums) {
            if(N < k)
                insert(i);
            else {
                if(i > heap[0]) {
                    delMin();
                    insert(i);
                }
            }
            // List<Integer> list = Arrays.asList(heap);
            // System.out.println("\ni:"+i+"N:"+N);
            // System.out.println(list);
        }
        return heap[0];
    }
}

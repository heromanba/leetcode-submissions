class Solution {
    private int[] heap;
    private int N;
    
    private void exch(int i, int j) {
        int tmp = heap[i];
        heap[i] = heap[j];
        heap[j] = tmp;
    }
    
    private void delMin() {
        heap[0] = heap[--N];
        sink(0);
    }
    
    private void insert(int v) {
        heap[N++] = v;
        swim(N-1);
    }
    
    private void sink(int i) {
        while(i<N) {
            int left = 2*(i+1)-1;
            int right = 2*(i+1);
            int child;
            if((right<N)&&(heap[right]<heap[left]))
                child = right;
            else if(left<N)
                child = left;
            else
                break;
            if(heap[child]<heap[i]) {
                exch(i, child);
                i = child;
            } else
                break;
        }
    }
    
    private void swim(int i) {
        while(i>=0) {
            int parent = (i+1)/2-1;
            if((parent>=0)&&(heap[parent]>heap[i])) {
                exch(parent, i);
                i = parent;
            } else
                break;
        }
    }
    
    public int kthLargestValue(int[][] matrix, int k) {
        heap = new int[k];
        
        int[][] xor = new int[matrix.length][matrix[0].length];
        for(int i=0; i<matrix.length; i++) {
            for(int j=0; j<matrix[0].length; j++) {
                xor[i][j] = matrix[i][j];
                if((j-1>=0))
                    xor[i][j]^=xor[i][j-1];
                if((i-1>=0))
                    xor[i][j]^=xor[i-1][j];
                if((i-1>=0)&&(j-1>=0)){
                    xor[i][j]^=xor[i-1][j-1];
                }
                
                if(N<k)
                    insert(xor[i][j]);
                else {
                    if(xor[i][j]>heap[0]) {
                        delMin();
                        insert(xor[i][j]);
                    }
                }
            }
        }
        // System.out.println(Arrays.asList(heap));
        return heap[0];
    }
}

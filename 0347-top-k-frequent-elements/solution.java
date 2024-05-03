class Solution {
    private int[][] heap;
    private int N = 0;
    
    private void exch(int i, int j) {
        int[] tmp = heap[j];
        heap[j] = heap[i];
        heap[i] = tmp;
    }
    
    private void sink(int i) {
        while(i < N) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int child;
            if((right<N)&&(heap[right][1]<heap[left][1]))
                child = right;
            else if (left<N)
                child = left;
            else
                break;
            if(heap[i][1]>heap[child][1]) {
                exch(child, i);
                i = child;
            } else
                break;
        }
    }
    
    private void swim(int i) {
        while(i >= 0) {
            int parent = (i+1)/2-1;
            if((parent >= 0)&& (heap[parent][1]>heap[i][1])) {
                exch(parent, i);
                i = parent;
            } else
                break;
        }
    }
    
    private void insert(int[] i) {
        heap[N++] = i;
        swim(N-1);
    }
    
    private void delMin() {
        heap[0] = heap[--N];
        sink(0);
    }
    
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        for(int i: nums) {
            if(counter.containsKey(i))
                counter.put(i, counter.get(i)+1);
            else
                counter.put(i, 1);
        }
        
        heap = new int[k][2];
        
        for(Map.Entry<Integer, Integer> entry: counter.entrySet()) {
            if(N<k) {
                int[] tmp = new int[2];
                tmp[0] = entry.getKey();
                tmp[1] = entry.getValue();
                insert(tmp);
            }
            else {
                if(entry.getValue()>heap[0][1]) {
                    delMin();
                    
                    int[] tmp = new int[2];
                    tmp[0] = entry.getKey();
                    tmp[1] = entry.getValue();
                    insert(tmp);
                }
            }
            // System.out.println(entry);
            // System.out.println(Arrays.deepToString(heap));
        }
        int[] ret = new int[k];
        int i = 0;
        for(int[] tmp: heap) {
            ret[i++] = tmp[0];
        }
        return ret;
    }
}

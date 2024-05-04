class Solution {
    private List<Map.Entry<String, Integer>> heap;
    private int N;
    
    Map<String, Integer> counter = new HashMap<>();
    
    private void exch(int i, int j) {
        Map.Entry<String, Integer> tmp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, tmp);
    }
    
    private void insert(Map.Entry<String, Integer> entry) {
        heap.set(N++, entry);
        swim(N-1);
    }
    
    private void delMin() {
        heap.set(0, heap.get(N-1));
        heap.set(N-1, null);
        N--;
        sink(0);
    }
    
    private void swim(int i) {
        while(i>=0) {
            int parent = (i+1)/2-1;
            if(
                (parent>=0)&&
                (!less(heap.get(parent).getKey(), heap.get(i).getKey()))
            ) {
                exch(parent, i);
                i = parent;
            } else
               break;
        }
    }
               
    private void sink(int i) {
        while(i < N) {
            int left = (i+1)*2-1;
            int right = (i+1)*2;
            int child;
            if(
                (right<N)&&
                (less(heap.get(right).getKey(),heap.get(left).getKey()))
            )
                child = right;
            else if(left<N)
                child = left;
            else
                break;
            if(!less(heap.get(i).getKey(), heap.get(child).getKey())) {
                exch(i, child);
                i = child;
            } else
                break;
                
        }
    }
    public List<String> topKFrequent(String[] words, int k) {
        for(String s: words) {
            if(counter.containsKey(s))
                counter.put(s, counter.get(s)+1);
            else
                counter.put(s, 1);
        }
        heap = new ArrayList<>(k);
        for(int i=0; i<k; i++)
            heap.add(null);
        for(Map.Entry<String, Integer> entry: counter.entrySet()) {
            if(N<k)
                insert(entry);
            else {
                if(!less(entry.getKey(), heap.get(0).getKey())) {
                    delMin();
                    insert(entry);
                }
            }
            // System.out.println(entry);
            // System.out.println(heap);
        }
        List<String> ret = new ArrayList<>(k);
        for(Map.Entry<String, Integer> entry: heap) {
            ret.add(entry.getKey());
        }
        
        Comparator<String> comp = new Comparator<>() {
            public int compare(String a, String b) {
                int freq = counter.get(b) - counter.get(a);
                if(freq==0)
                    return a.compareTo(b);
                else
                    return freq;
            }
        };
        Collections.sort(ret, comp);
        return ret;
    }
    
    private boolean less(String a, String b) {
        int freq = counter.get(a) - counter.get(b);
        if(freq!=0)
            return freq<0;
        return a.compareTo(b)>0;
    }
}

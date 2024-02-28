class CustomStack {
    int[] data = null;
    int size = 0;
    
    public CustomStack(int maxSize) {
        data = new int[maxSize];
    }
    
    public void push(int x) {
        if (size < data.length) {
            data[size] = x;
            size += 1;
        }
    }
    
    public int pop() {
        if (size > 0) {
            return data[--size];  
        }
        return -1;
    }
    
    public void increment(int k, int val) {
        if (k > size) {
            k = size;
        }
        for (int i=0; i<k; i++) {
            data[i] += val;
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */

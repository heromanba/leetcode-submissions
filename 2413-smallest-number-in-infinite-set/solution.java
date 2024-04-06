class SmallestInfiniteSet {
    private Set<Integer> popped = new HashSet<>();
    private int smallest = 1;
        
    public SmallestInfiniteSet() {
        
    }
    
    public int popSmallest() {
        int old = smallest;
        
        popped.add(smallest);
        
        while(popped.contains(smallest))
            smallest++;
        
        return old;
    }
    
    public void addBack(int num) {
        if((num>smallest)&&(!popped.contains(num)))
            return;
        else if((num>smallest)&&(popped.contains(num)))
            popped.remove(num);
        else if(num<=smallest) {
            popped.remove(num);
            smallest = num;
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */

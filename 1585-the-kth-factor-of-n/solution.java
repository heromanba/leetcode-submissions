class Solution {
    public int kthFactor(int n, int k) {
        if(n==1)
            return 1;
        Set<Integer> first=new HashSet<>();
        //List<Integer> second=new ArrayList<>();
        int half=(int)Math.ceil((float)n/2);
        for(int i=1; i<=half; i++){
            if(n%i==0){
                first.add(i);
                first.add(n/i);
            }
        }
        //System.out.println(first);
        List<Integer> second=new ArrayList<>();
        second.addAll(first);
        Collections.sort(second);
        if(k<=second.size())
            return second.get(k-1);
        //else if(k<=first.size()+second.size())
        //    return second.get(second.size()-(k-first.size()));
        else 
            return -1;
    }
}

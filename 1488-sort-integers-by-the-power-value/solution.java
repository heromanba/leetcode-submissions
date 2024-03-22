class Solution {
    public int getKth(int lo, int hi, int k) {
        mem.put(1,0);
        List<Integer> tmp=new ArrayList<Integer>();
        for(int i=lo;i<=hi;i++){
            getScore(i);
            tmp.add(i);
        }
        Comparator<Integer> comp=new Comparator<Integer>(){
            public int compare(Integer a, Integer b) {
               return mem.get(a)-mem.get(b);
           }
        };
        Collections.sort(tmp, comp);
        //System.out.println(mem.get(k));
        return tmp.get(k-1);
    }
    
    private Map<Integer,Integer> mem=new HashMap<>();
    
    private int getScore(int i) {
        Stack<Integer> s=new Stack<>();
        int score=0;
        while(i!=1){
            if(!mem.containsKey(i)){
                s.push(i);
                if(i%2==0)
                    i/=2;
                else
                    i=3*i+1;
            } else {
                score = mem.get(i);
                break;
            }
        }
        while(!s.isEmpty()) {
            int j=s.pop();
            score+=1;
            mem.put(j,score);
        }
        return score;
    }
}

class Solution {
    private List<List<Integer>> ret = new ArrayList<>();
    
    public List<List<Integer>> combine(int n, int k) {
        List<Integer> curr = new ArrayList<>(k);
        List<Integer> candidates = new ArrayList<>(n);
        for(int i=1; i<=n; i++)
            candidates.add(i);
        
        backtrack(curr, candidates, k);
        return ret;
    }
    
    private void backtrack(List<Integer> curr, List<Integer> candidates, int k) {
        if(curr.size()==k) {
            ret.add(curr);
            return;
        }
        for(int i=0; i<candidates.size(); i++) {
            List<Integer> next = new ArrayList<>();
            next.addAll(curr);
            next.add(candidates.get(i));
            
            List<Integer> newCandidates = candidates.subList(i+1, candidates.size());
            
            backtrack(next, newCandidates, k);
        }
        return;
    }
    
}

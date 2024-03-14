class Solution {
    public int[] restoreArray(int[][] adjacentPairs) {
        Map<Integer, List<Integer>> adjList = new HashMap<>();
        for (int[] pair: adjacentPairs) {
            
            if (!adjList.containsKey(pair[0])) {
                List<Integer> tmp = new ArrayList<>();
                tmp.add(pair[1]);
                adjList.put(pair[0], tmp);
            } else
                adjList.get(pair[0]).add(pair[1]);
            
            if (!adjList.containsKey(pair[1])) { 
                List<Integer> tmp = new ArrayList<>();
                tmp.add(pair[0]);
                adjList.put(pair[1], tmp);
            }
            else
                adjList.get(pair[1]).add(pair[0]);
            
        }
        // System.out.println(adjList);
        Integer start = null;
        for (Map.Entry<Integer, List<Integer>> entry: adjList.entrySet()) {
            if (entry.getValue().size()==1) {
                start = entry.getKey();
                break;
            }
            
        }
        Set<Integer> visited = new HashSet<>();
        
        int[] ret = new int[adjacentPairs.length+1];
            
        Integer curr = start;
        ret[0] = start;
        visited.add(start);
        for (int i=1; i<ret.length; i++) {
            List<Integer> adjs = adjList.get(curr);
            
            for (int val: adjs) {
                if (!visited.contains(val)) {
                    ret[i] = val;
                    curr = val;
                    visited.add(val);
                    break;
                }
            }
        }
        return ret;
    }
}

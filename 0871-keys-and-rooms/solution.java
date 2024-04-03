class Solution {
    private Set<Integer> visited = new HashSet<>();
    
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        dfs(rooms, 0);
        return visited.size() == rooms.size();
    }
    
    private void dfs(List<List<Integer>> rooms, int key) {
        if (visited.contains(key))
            return;
        visited.add(key);
        if (rooms.get(key).isEmpty())
            return;
        for(int newKey: rooms.get(key)) {
            dfs(rooms, newKey);
        }
    }
}

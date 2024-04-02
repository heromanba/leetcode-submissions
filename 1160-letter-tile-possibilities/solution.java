class Solution {
    public int numTilePossibilities(String tiles) {
        Map.Entry<String, String> root = Map.entry("", tiles);
        
        Set<Map.Entry<String, String>> currLevel = new HashSet<>();
        currLevel.add(root);
        
        int ret = 0;
        while(!currLevel.isEmpty()) {
            Set<Map.Entry<String, String>> nextLevel = new HashSet<>();
            Set<String> tmp = new HashSet<>();
            for(Map.Entry<String,String> node: currLevel) {
                String oldKey = node.getKey();
                String oldValue = node.getValue();
                for(int i=0; i<oldValue.length(); i++) {
                    String newKey = oldKey+oldValue.charAt(i);
                    String newValue = oldValue.substring(0,i) + oldValue.substring(i+1,oldValue.length());
                    nextLevel.add(Map.entry(newKey, newValue));
                    tmp.add(newKey);
                }
            }
            currLevel = nextLevel;
            ret += tmp.size();
        }
        return ret;
    }
}

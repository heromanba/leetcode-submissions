class Solution {
    Set<List<String>> ret = new HashSet<>();
    Map<String, Boolean> mem = new HashMap<>();
    Map<List<String>, List<List<String>>> partsMem = new HashMap<>();
    
    public List<List<String>> partition(String s) {
        List<String> root = new ArrayList<>();
        root.add(s);
        
        List<List<String>> currLevel = new ArrayList<>();
        currLevel.add(root);
        
        while(!currLevel.isEmpty()) {
            List<List<String>> nextLevel = new ArrayList<>();
            for(List<String> node: currLevel) {
                boolean allPalindrome = true;
                for(String ss: node) {
                    if (!isPalindrome(ss)) {
                        allPalindrome = false;
                        break;
                    }
                }
                if(allPalindrome) {
                    // Set<String> tmp = new HashSet<>();
                    // tmp.addAll(node);
                    ret.add(node);
                }
                
                List<List<String>> nodeParts = new ArrayList<>();
                if(partsMem.containsKey(node)) {
                    continue;
                } else {
                    for(int i=0; i<node.size(); i++) {
                        String ss = node.get(i);
                        if(ss.length() > 1) {
                            for(int j=1; j<ss.length(); j++) {
                                List<String> tmp = new ArrayList<>();
                                for(int k=0; k<node.size(); k++) {    
                                    if(i!=k) {
                                        tmp.add(node.get(k));
                                    } else {
                                        tmp.add(ss.substring(0, j));
                                        tmp.add(ss.substring(j, ss.length()));
                                    }
                                }
                                nodeParts.add(tmp);
                            }
                        }
                    }
                    nextLevel.addAll(nodeParts);
                    partsMem.put(node, nodeParts);
                }
            }
            currLevel = nextLevel;
        }
        // System.out.println(mem);
        List<List<String>> retList = new ArrayList<>();
        for(List<String> tmp: ret){
            retList.add(tmp);
        }
        return retList;
        
    }
    
    private boolean isPalindrome(String s) {
        if(mem.containsKey(s))
            return mem.get(s);
        
        if(s.length()==1) {
            boolean tmp=true;
            mem.put(s, tmp);
            return tmp;
        }
        if(s.length()==2) {
            boolean tmp = s.charAt(0)==s.charAt(1);
            mem.put(s, tmp);
            return tmp;
        }
        if(s.charAt(0)==s.charAt(s.length()-1)) {
            boolean tmp = isPalindrome(s.substring(1,s.length()-1));
            mem.put(s, tmp);
            return tmp;
        }
        mem.put(s, false);
        return false;
    }
}

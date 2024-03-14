class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> counter = new HashMap<>();
        for (Character c: s.toCharArray()) {
            if (!counter.containsKey(c))
                counter.put(c, 1);
            else 
                counter.put(c, counter.get(c)+1);
        }
        List<Character> keys = new ArrayList<>();
        for (Character k: counter.keySet())
            keys.add(k);
        Comparator<Character> comp = new Comparator<>() {
            public int compare(Character a, Character b) {
                return counter.get(b) - counter.get(a);
            }
        };
        Collections.sort(keys, comp);
        
        StringBuilder sb = new StringBuilder();
        for (Character k: keys) {
            int n = counter.get(k);
            for (int i=0; i<n; i++) 
                sb.append(k);
        }
        return sb.toString();
            
    }
}

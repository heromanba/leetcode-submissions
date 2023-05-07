class Solution {
    public int longest = 0;

    public void recur(String s, int k, int l, int r) {
        Map<Character, List<Integer>> cnt = new HashMap<>();
        for(int i=l; i<r; i++) {
            Character c = s.charAt(i);
            if (!cnt.containsKey(c)) {
                List<Integer> list = new ArrayList<>();
                list.add(i);
                cnt.put(c, list);
            } else {
                cnt.get(c).add(i);
            }
        }
        List<Integer> parts = new ArrayList<Integer>();
        for(Character c: cnt.keySet()) {
            if (cnt.get(c).size() < k) {
                parts.addAll(cnt.get(c));
            }
        }
        if (parts.isEmpty() && ((r-l)>longest)) {
            longest = r-l;
            return;
        }
        if (!parts.isEmpty()) {
            if (l < parts.get(0))
                recur(s, k, l, parts.get(0));
            for(int i=0; i<parts.size()-1; i++) {
                recur(s, k, parts.get(i)+1, parts.get(i+1));
            }
            if (r > parts.get(parts.size()-1))
                recur(s, k, parts.get(parts.size()-1)+1, r);
        }
        return;
    }
    public int longestSubstring(String s, int k) {
        recur(s, k, 0, s.length());
        return longest;
    }
}

class Solution {
    public Map<Character, Pair<Integer, Integer>> range = new HashMap<>();

    public List<Integer> partitionLabels(String s) {
        for(int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (!range.containsKey(c)) {
                range.put(c, new Pair<Integer, Integer>(i, i));
            } else {
                Integer start = range.get(c).getKey();
                range.put(c, new Pair<Integer, Integer>(start, i));
            }
        }
        List<Integer> ret = new ArrayList<>();
        ret.add(-1);
        for(int i=0; i<s.length(); i++) {
            boolean isGoodPivot = true;
            List<Integer> tmp = new ArrayList<>();
            for(Character c: range.keySet()) {
                Integer start = range.get(c).getKey();
                Integer end = range.get(c).getValue();
                if ((start<=i) && (i<end)) {
                    isGoodPivot = false;
                    break;
                }
                else {
                    tmp.add(i);
                }
            }
            if (isGoodPivot) {
                ret.add(i);
                range.keySet().removeAll(tmp);
            }
        }
        List<Integer> result = new ArrayList<Integer>();
        for (int i=0; i<ret.size()-1; i++)
            result.add(ret.get(i+1)-ret.get(i));
        return result;
    }
}

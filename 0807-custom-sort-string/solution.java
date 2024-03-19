class Solution {
    public String customSortString(String order, String s) {
        Map<Character, Integer> cnt = new HashMap<Character, Integer>(order.length(), 1.0f);
        for (Character c: order.toCharArray()) {
            cnt.put(c, 0);
        }
        StringBuilder anyOrder = new StringBuilder();
        for (Character c: s.toCharArray()) {
            if (!cnt.containsKey(c))
                anyOrder.append(c);
            else
                cnt.put(c, cnt.get(c)+1);
        }
        StringBuilder ret = new StringBuilder();
        for (Character c: order.toCharArray()) {
            for (int i=0; i<cnt.get(c); i++) {
                ret.append(c);
            }
        }
        ret.append(anyOrder);
        return ret.toString();
    }
}

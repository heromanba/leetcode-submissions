class Solution {
    private int[] id;
    
    public String smallestEquivalentString(String s1, String s2, String baseStr) {
        id = new int[26];
        for (int i=0; i<26; i++) {
            id[i]=i;
        }
        for (int i=0; i<s1.length(); i++) {
            char c1 = s1.charAt(i);
            char c2 = s2.charAt(i);
            int pid = Math.max(id[c1-'a'], id[c2-'a']);
            int qid = Math.min(id[c1-'a'], id[c2-'a']);
            for (int j=0; j<id.length; j++) {
                if (id[j]==pid) id[j]=qid;
            }
        }
        List<Integer> arr = new ArrayList<>();
        for (int i: id) {
            arr.add(i);
        }
        for (int i=0; i<baseStr.length(); i++) {
            char c = (char)((int)'a'+id[baseStr.charAt(i)-'a']);
            baseStr = baseStr.substring(0,i) + c + baseStr.substring(i+1);
        }
        return baseStr;
    }
}

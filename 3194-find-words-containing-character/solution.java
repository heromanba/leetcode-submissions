class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        List<Integer> ret = new ArrayList<>();
        for (int i=0; i<words.length; i++) {
            if (words[i].indexOf(x) != -1)
                ret.add(i);
        }
        return ret;
    }
}

class Solution {
    public boolean halvesAreAlike(String s) {
        int half = s.length() / 2;
        int first = 0;
        int second = 0;
        Set<Character> vowelSet = Set.of('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');
        for(int i=0; i<s.length(); i++) {
            Character c = s.charAt(i);
            if (vowelSet.contains(c)) {
                if (i < half) {
                    first += 1;
                } else {
                    second += 1;
                }
            }
        }
        return first == second;
    }
}

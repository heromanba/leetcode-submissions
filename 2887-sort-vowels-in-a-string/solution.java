class Solution {
    public String sortVowels(String s) {
        Set<Character> vowels = Set.of('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u');
        List<Character> vowelsInInput = new ArrayList<>();
        for (Character c: s.toCharArray()) {
            if (vowels.contains(c)) {
                vowelsInInput.add(c);
            }
        }
        Collections.sort(vowelsInInput);
        
        StringBuilder sb = new StringBuilder();
        
        int i = 0;
        // Appends characters one by one
        for (char c: s.toCharArray()) {
            if (vowels.contains(c)) {
                c = vowelsInInput.get(i);
                i += 1;
            }
            sb.append(c);
        }
        return sb.toString();
    }
}

class Solution {
    public String convertToTitle(int columnNumber) {
        List<Character> retValArr = new ArrayList<>();
        while (columnNumber > 0) {
            retValArr.add( (char) ((columnNumber-1) % 26 + 65) );
            columnNumber = (columnNumber-1) / 26;
        }
        Collections.reverse(retValArr);
        return retValArr.stream().map(Object::toString)
                        .collect(Collectors.joining(""));
    }

}

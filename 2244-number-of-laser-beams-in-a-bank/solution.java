class Solution {
    public int numberOfBeams(String[] bank) {
        int numB = 0;
        int prev = 0;
        for (String row: bank) {
            int num1 = 0;
            for (char c: row.toCharArray()) {
                if (c == '1') {
                    num1 += 1;
                }
            }
            if (num1 > 0) {
                if (prev > 0) {
                    numB += prev * num1;
                    prev = num1;
                } else {
                    prev = num1;
                }
            }
        }
        return numB;
    }
}

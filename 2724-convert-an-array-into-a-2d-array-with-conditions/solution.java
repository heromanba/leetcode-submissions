class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        List<Set<Integer>> temp = new ArrayList<>();
        for (int n: nums) {
            boolean needsToAddRow = true;
            for (Set<Integer> row: temp) {
                if (!row.contains(n)) {
                    row.add(n);
                    needsToAddRow = false;
                    break;
                }
                // System.out.println(temp);
                // System.out.println(row);
                // System.out.println(n);
            }
            if (needsToAddRow) {
                Set<Integer> row = new HashSet<>();
                row.add(n);
                temp.add(row);
            }
        }
        List<List<Integer>> ret = new ArrayList<>();
        for (Set<Integer> row: temp) {
            ret.add(new ArrayList<>(row));
        }
        return ret;
    }
}

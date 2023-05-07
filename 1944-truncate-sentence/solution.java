class Solution {
    public String truncateSentence(String s, int k) {
        String[] a = s.split(" ");
        int idx = k;
        for(int i=1; i<a.length; i++) {
            // if(Character.isUpperCase(a[i].charAt(0))) {
            //     idx = i;
            //     break;
            // }
            if (i>k) {
                break;
            }
        }
        System.out.println(idx);
        return String.join(" ", Arrays.copyOfRange(a, 0, idx));
    }
}

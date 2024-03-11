class Solution {
    public int[][] reconstructQueue(int[][] people) {
        Comparator<int[]> comp = new Comparator<>() {
            public int compare(int[] a, int[] b) {
                if (a[0]>b[0]) return -1;
                if (a[0]<b[0]) return 1;
                if (a[1]>b[1]) return 1;
                if (a[1]<b[1]) return -1;
                return 0;
            }
        };
        
        Arrays.sort(people, comp);
        for (int i=0; i<people.length; i++) {
            int posToMove = i - people[i][1];
            int[] temp = people[i];
            for (int j=i; j>i-posToMove; j--) {
                people[j]=people[j-1];
            }
            people[i-posToMove]=temp;
        }
        return people;
    }
}

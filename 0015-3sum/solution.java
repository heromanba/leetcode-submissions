class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        QuickSort.sort(nums);
        Set<List<Integer>> tmp1 = new HashSet<>();
        for(int i=0; i<nums.length-2; i++) {
            for(int j=i+1; j<nums.length-1; j++) {
                int target = -(nums[i]+nums[j]);
                int idx = BinarySearch.search(nums, j+1, target);
                if (idx!=-1) {
                    List<Integer> tmp2 = List.of(nums[i], nums[j], nums[idx]);
                    tmp1.add(tmp2);
                }
            }
        }
        List<List<Integer>> ret = new ArrayList<>();
        for(List<Integer> tmp3: tmp1) {
            ret.add(tmp3);
        }
        return ret;
    }
}

class BinarySearch {
    public static int search(int[] a, int lo, int v) {
        int hi = a.length-1;
        while(lo<=hi) {
            int mid = lo + (hi-lo)/2;
            if(a[mid]>v) hi=mid-1;
            else if (a[mid]<v) lo=mid+1;
            else return mid;
        }
        return -1;
    }
}

class QuickSort {
    public static void sort(int[] a) {
        int n = a.length;// shuffle, then sort
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            int oi = random.nextInt(n), temp = a[oi];
            a[oi] = a[i];
            a[i] = temp;
        }
        sort(a, 0, a.length-1);
    }
    
    private static void sort(int[] a, int lo, int hi) {
        if(hi<=lo) return;
        int j = partition(a, lo, hi);
        sort(a, lo, j-1);
        sort(a, j+1, hi);
    }
    
    private static int partition(int[] a, int lo, int hi) {
        int v = a[lo];
        int i=lo, j=hi+1;
        while(true) {
            while(a[++i]<v)
                if(i==hi) break;
            while(v<a[--j])
                if(j==lo) break;
            if(i>=j) break;
            exch(a, i, j);
        }
        exch(a, j, lo);
        return j;
    }
    
    private static void exch(int[] a, int i, int j) {
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
}

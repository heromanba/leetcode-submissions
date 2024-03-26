class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        // Arrays.sort(arr);
        int ret = 0;
        for(int i=arr.length-1; i>=k-1; i--){
            int sum = 0;
            for(int j=i; j>=i-k+1; j--)
                sum += arr[j];
            // System.out.print("i:"+(float)sum/k);
            if((float)sum/k >= threshold)
                ret += 1;
        }
        return ret;
        
    }
}

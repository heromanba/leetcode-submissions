class Solution {
private:
    void mergeSort(vector<int>& A, int lo, int hi)
    {
        if (hi - lo < 2) return;
        int mi = (hi + lo) >> 1;
        mergeSort(A, lo, mi);
        mergeSort(A, mi, hi);
        merge(A, lo, mi, hi);
    }
    
    void merge(vector<int>& A, int lo, int mi, int hi)
    {
        int lb = mi - lo;
        int lc = hi - mi;
        
        int B[lb];
        for (int i = 0; i < lb; i++)
            B[i] = A[lo + i];
        
        for (int i = lo, j = 0, k = mi; (j < lb) || (k < hi);)
        {
            if ((j < lb) && (hi <= k || (B[j] <= A[k])))
                A[i++] = B[j++];
            if ((k < hi) && (lb <= j || (A[k] < B[j])))
                A[i++] = A[k++];
        }
    }

public:
    vector<int> sortedSquares(vector<int>& A) {
        for (int i = 0; i < A.size(); i++)
            A[i] = A[i] * A[i];
        mergeSort(A, 0, A.size());
        return A;
    }
};

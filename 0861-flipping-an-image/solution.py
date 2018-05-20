class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        import numpy
        for i in range(len(A)):
            A[i] = A[i][::-1]
            for j in range(len(A[i])):
                A[i][j] = int(A[i][j] == 0)
        return A
        

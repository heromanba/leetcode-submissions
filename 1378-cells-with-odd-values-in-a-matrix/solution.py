class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        nums = [[0 for j in range(m)] for i in range(n)]
        print(indices)
        for idx_pair in indices:
            ri, ci = idx_pair
            for j in range(m):
                nums[ri][j] += 1
            for i in range(n):
                nums[i][ci] += 1
        num_odd = 0
        for i in range(n):
            for j in range(m):
                if nums[i][j] % 2 != 0:
                    num_odd += 1
        return num_odd

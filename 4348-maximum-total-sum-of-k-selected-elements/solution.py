from heapq import heappush, heappop
class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        min_heap = []
        for n in nums:
            if len(min_heap) < k:
                heappush(min_heap, n)
            elif n > min_heap[0]:
                    heappop(min_heap)
                    heappush(min_heap, n)
        min_heap = sorted(min_heap, reverse=True)    
        ret = 0
        for n in min_heap:
            if mul > 0:
                ret += n * mul
            else:
                ret += n
            mul -= 1
        return ret

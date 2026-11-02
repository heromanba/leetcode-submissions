import heapq

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_heap = []
        for i in range(k-1):
            heapq.heappush(max_heap, (-nums[i], i))
        
        result = []
        for i in range(k-1, len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            while not (i-k+1 <= max_heap[0][1] <= i):
                heapq.heappop(max_heap)
            result.append(-max_heap[0][0])

        return result



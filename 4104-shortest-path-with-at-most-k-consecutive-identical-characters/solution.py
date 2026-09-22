import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n==1 and len(edges) == 0:
            return 0
        graph = [[] for _ in range(n)]

        for i in range(len(edges)):
            u, v, w = edges[i]
            graph[u].append((v, w, labels[v]))
        
        dist_list = [[float('inf') for _ in range(k+1)] for _ in range(n)]
                
        # (dist, node, last_label, label_len)
        heap = [(0, 0, labels[0], 1)]
        while len(heap) > 0:
            top = heapq.heappop(heap)
            dist, node, last_label, label_len = top
            
            for v, w, label in graph[node]:
                if label == last_label and label_len + 1 > k:
                    continue
                    
                if label == last_label:
                    new_label_len = label_len+1
                else:
                    new_label_len = 1
                
                if dist + w < dist_list[v][new_label_len]:
                    dist_list[v][new_label_len] = dist + w
                    heapq.heappush(heap, (dist+w, v, label, new_label_len ))
        ret = min(dist_list[-1])
        return -1 if ret == float('inf') else ret



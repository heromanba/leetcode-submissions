from collections import defaultdict

class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        tree_graph = defaultdict(list)
        for parent, child in edges:
            tree_graph[parent].append(child)
        def dfs(node):
            if node not in tree_graph:
                return baseTime[node]
            earliest = float('inf')
            latest = float('-inf')
            for child in tree_graph[node]:
                finish_time = dfs(child)
                earliest = min(finish_time, earliest)
                latest = max(finish_time, latest)
            return latest - earliest + baseTime[node] + latest
        return dfs(0)

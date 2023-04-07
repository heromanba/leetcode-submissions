class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        # iterate all vertices and adjacent list
        def dfs(v, graph, path):
            adj = graph[v]
            if v == len(graph) - 1:
                paths.append(path + [v])
                return
                
            for adj_v in adj:
                dfs(adj_v, graph, path + [v])
        dfs(0, graph, [])
        return paths

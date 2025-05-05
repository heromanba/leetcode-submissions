class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True
        # initialize the graph
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)
        # detect if there is a cycle
        on_stack = [ False for _ in range(numCourses) ]
        visited = set()
        for s in range(numCourses):
            if s not in visited:
                # do dfs for each node
                stack = []
                stack.append( (s, False) )
                while stack:
                    curr_node, processed = stack.pop()
                    if processed:
                        on_stack[curr_node] = False
                    else:
                        # found a cycle
                        if curr_node in visited and on_stack[curr_node]:
                            return False
                        # avoid reprocessing visited nodes
                        if curr_node not in visited:
                            visited.add(curr_node)
                            on_stack[curr_node] = True
                            stack.append((curr_node, True))
                            for neighbor in graph[curr_node]:
                                stack.append((neighbor, False))
        return True

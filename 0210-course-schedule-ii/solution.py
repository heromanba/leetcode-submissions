class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return list(range(numCourses))
        # initialize the graph
        graph = [ [] for _ in range(numCourses) ]
        for a, b in prerequisites:
            graph[a].append(b)
        ret = []
        visited = set()
        on_stack = [ False for _ in range(numCourses) ]
        for s in range(numCourses):
            if s not in visited:
                stack = [ (s, False) ]
                while stack:
                    curr_node, processed = stack.pop()
                    if processed:
                        on_stack[curr_node] = False
                        ret.append(curr_node)
                    else:
                        if curr_node in visited and on_stack[curr_node]:
                            return []
                        if curr_node not in visited:
                            visited.add(curr_node)
                            on_stack[curr_node] = True
                            stack.append((curr_node, True))
                            for neighbor in graph[curr_node]:
                                stack.append((neighbor, False))
        return ret
                







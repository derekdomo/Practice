class Solution:
    def validTree(self, n, edges):
        # for a tree, each node must have one edge
        if n == 0:
            return True

        if len(edges) != n-1:
            return False

        graph = defaultdict(list)
        for u, v in edges:
           graph[u].append(v)
           graph[v].append(u)
        

        # if we can dfs the graph without revisting, then it means there
        # is no cycle, then a tree
        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if neighbor in visited or not dfs(neighbor, node):
                    return False

            return True
        

        if not dfs(0, -1):
            return False

        return len(visited) == n

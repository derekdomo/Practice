class Solution:
    def countComponents(self, n, edges):
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])


        def dfsVisit(graph, n, visited):
            visited.append(n)
            for neighbor in graph[n]:
                dfsVisit(graph, neighbor, visited)

            return

        visited = set()
        components = 0
        for i in range(n):
            if i not in visited:
                dfsVisit(graph, i, visited)
                components += 1

        return components

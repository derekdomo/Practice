'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.
'''
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbord = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        if node == None:
            return None
        def dfs(node, visited):
            visited[node] = Node(node.val)
            for n in node.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    dfs(n, visited)
                visited[node].neighbors.append(visited[n])

        dfs(node, visited)
        return visited[node]


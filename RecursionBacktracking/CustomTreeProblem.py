class Solution:
    def generate_tree(self, tree_edges):
        start_edge = tree_edges[0]
        visited = {}
        start_edge = " --->"+start_edge.split("--->")[0]
        self.dfs_helper(start_edge, 0, tree_edges, visited)

    def dfs_helper(self, start_edge, indent, tree_edges, visited):
        if start_edge in visited:
            print "cycle detected"
            return
        start, end = start_edge.split("--->")
        print "    |"*indent + "--->" + end 
        visited[start_edge] = True
        for edge in tree_edges:
            if edge in visited:
                continue
            start = edge.split("--->")[0]
            if start == end:
                self.dfs_helper(edge, indent+1, tree_edges, visited)


if __name__ == '__main__':
    sol = Solution()
    tree_edges = [
        "a--->b",
        "b--->c",
        "a--->d",
        "d--->e",
        "e--->f"
    ]
    sol.generate_tree(tree_edges)


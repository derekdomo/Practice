'''
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
'''
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        set_a = {}
        set_b = {}

        for i, n in enumerate(graph):
            for c_n in n:
                if c_n in set_a:
                    if i in set_a:
                        return False
                    set_b[i] = True
                elif c_n in set_a:
                    if i in set_b:
                        return False
                    set_a[i] = True
                else:
                    if i in set_a:
                        set_b[c_n] = True
                    elif i in set_b:
                        set_a[c_n] = True
                    else:
                        set_a[i] = True
                        set_b[c_n] = False
        return True
        
#sol = Solution()
#print sol.isBipartite([[1,3], [0,2], [1,3], [0,2]])
#print sol.isBipartite([[1,2,3], [0,2], [0,1,3], [0,2]])

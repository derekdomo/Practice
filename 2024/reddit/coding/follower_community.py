'''
We have communities with IDs C1,C2,... and followers with IDs F1,F2,..., where each user can follow any of the communities.

We would like to find “similar” or “related” communities by finding all communities that share followers with the input one, Cx. Implement a function to return all related communities of Cx.

Example:
Community -> follower data:
C1: [F1, F3]
C2: [F1, F2]
C3: [F2]
C4: [F3]

Follower -> community data (mirrored data):
F1: [C1, C2]
F2: [C2, C3]
F3: [C1, C4]

get_related_communities(C4) -> [C1]
get_related_communities(C2) -> [C1,C3]

Assume the data for both maps is pre populated and you can use it for the problem.

Part 2:
Now, we want to explore communities which might not share followers directly but
are related by indirect relationships (eg. C4 is indirectly related to C2 through C1). 
Extend the solution to accept degrees of indirect relationship as an input. 
Each degree adds to the result the communities directly related (sharing followers) to the communities from the previous degrees. Please note that we’re interested in related communities up-to a specific degree (as opposed to only at a specific degree).

Example:
get_related_communities_with_degree(C4, 1) -> [C1]
get_related_communities_with_degree(C4, 2) -> [C1, C2]

community_map = {
'C1': ['F1', 'F3'],
'C2': ['F1', 'F2'],
'C3': ['F2'],
'C4': ['F3'],
}

follower_map = {
'F1': ['C1', 'C2'],
'F2': ['C2', 'C3'],
'F3': ['C1', 'C4'],
}
'''
class Solution:
    def get_related_communities(self, c, follower_data, community_data):
        communities = set([c])
        for follower in follower_data[c]:
            for rel_c in community_data[follower]:
                communities.add(rel_c)

        communities.remove(c)
        return list(communities)
    

    def get_related_communities_with_degrees(self, c, degree, follower_data, community_data):
        from collections import deque
        queue = deque([c])
        result = set()
        while len(queue) > 0:

        return list(res)


sol = Solution()
print(
        sol.get_related_communities_with_degrees(
                'C4', 1,
                {
                    'C1': ['F1', 'F3'],
                    'C2': ['F1', 'F2'],
                    'C3': ['F2'],
                    'C4': ['F3'],
                },
                {
                    'F1': ['C1', 'C2'],
                    'F2': ['C2', 'C3'],
                    'F3': ['C1', 'C4'],
                },
            )
        )




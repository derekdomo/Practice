'''
There are a total of numCourses courses you have to take, labeled from 0 to 
numCourses - 1. You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''
class Solution:
    def canFinish(self, num_courses, prerequisites):
        # build a adjacent matrix of a course and the courses it requires
        # also build a dictionary of a course and how many it is requires
        indegress = {}
        adj = {}
        for prereq in prerequisites:
            if prereq[1] not in adj:
                adj[prereq[1]] = [prereq[0]]
            else:
                adj[rereq[1]].append(prereq[0])
            if prereq[0] in indegrees:
                indegrees[prereq[0]] = 1
            else:
                indegrees[prereq[0]] += 1

        q = []
        for i in num_courses:
            if i not in indegrees:
                q.append(i)

        n_courses = 0
        while len(q) > 0:
            n = q.pop()
            n_courses += 1
            
            for nb in adj[n]:
                indegrees[nb] -= 1
                if indegrees[nb] == 0:
                    q.append(nb)

        return n_courses == num_courses



'''
339. Nested List Weight Sum
Medium
Topics
Companies
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

 

Example 1:


Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
Example 2:


Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
Example 3:

Input: nestedList = [0]
Output: 0
 

Constraints:

1 <= nestedList.length <= 50
The values of the integers in the nested list is in the range [-100, 100].
The maximum depth of any integer is less than or equal to 50.
'''

class Solution:
    def sumWeights(self, lists):
        def sumWeightsWithWeight(l, multiplier):
            cur_sum = 0
            for i in l:
                if type(i) is list:
                    cur_sum += sumWeightsWithWeight(i, multiplier+1)
                else:
                    cur_sum += i * multiplier
            return cur_sum

        return sumWeightsWithWeight(lists, 1)


sol = Solution()
print(sol.sumWeights([[1,1],2,[1,1,]]))
print(sol.sumWeights([1,[4,[6]]]))
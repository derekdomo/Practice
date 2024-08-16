"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""
class Solution:
    def solve(self, s):
        bracket_map = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        stack = []
        for c in s:
            if c in bracket_map:
                expect_bracket = bracket_map[c]
                if expect_bracket == stack[-1]:
                    # we check if the what we see has a closing bracker
                    # if we has, we pop the stack
                    stack.pop()
                    continue
                else:
                    # if we dont, we found a mismatch
                    return False
            else:
                # if the c is not a closing bracet, we push to the stack
                stack.append(c)

        return True


sol = Solution()
print(sol.solve('()[]{}'))

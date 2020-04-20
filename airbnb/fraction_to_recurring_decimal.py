'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ret = ""
        if numerator >= denominator:
            ret += str(numerator/denominator)
            numerator = numerator % denominator
        else:
            ret += '0'
        
        if numerator == 0:
            return ret

        # find recursion part
        initial = numerator
        recursion = str(numerator * 10 / denominator) 
        numerator = numerator * 10 % denominator
        rec = {initial:0}
        while numerator != 0:
            print numerator, rec
            if numerator in rec:
                recursion = recursion[:rec[numerator]] + "(" + recursion[rec[numerator]:]  + ")"
                break
            rec[numerator] = len(recursion)
            recursion += str(numerator * 10 / denominator)
            numerator = numerator * 10 % denominator

        return ret + '.' + recursion

if __name__ == '__main__':
    sol = Solution()
    print sol.fractionToDecimal(1, 6)


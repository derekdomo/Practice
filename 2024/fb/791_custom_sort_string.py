class Solution:
    def customSortString(self, order, s):
        order_dict = {}
        for i, c in enumerate(order):
            order_dict[c] = i

        char_with_order = []
        for c in s:
            char_with_order.append((order_dict.get(c, -1), c))

        char_with_order = sorted(char_with_order, key=lambda x: x[0])
        return ''.join([x for _, x in char_with_order])

sol = Solution()
print(sol.customSortString('cba', 'abcd'))

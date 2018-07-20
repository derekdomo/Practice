class Solution:
    valid_operator = ['*', '-', '+', '/']
    def minimum_edit_reverse_polish_notation(self, arr):
        num_operations = 0
        if len(arr) == 1:
            if arr[0].isdigit():
                return 0
            else:
                return 1
        if arr[-1] not in self.valid_operator:
            num_operations += 1
        minimum_edit = 1000000 
        for i in xrange(1, len(arr)-1):
            left = self.minimum_edit_reverse_polish_notation(arr[0:i])
            right = self.minimum_edit_reverse_polish_notation(arr[i:-1])
            minimum_edit = min(minimum_edit, left+right)
        return minimum_edit + num_operations

if __name__ == '__main__':
    sol = Solution()
    print sol.minimum_edit_reverse_polish_notation(['1', '2', '*'])
    print sol.minimum_edit_reverse_polish_notation(['1', '*', '2'])
    print sol.minimum_edit_reverse_polish_notation(['1', '2', '*', '23', '4'])

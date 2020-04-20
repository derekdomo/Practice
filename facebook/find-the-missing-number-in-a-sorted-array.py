'''
[0,1,2,4]
'''
def find_missing_number(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right - left) / 2
        if arr[mid] == mid:
            # missing integer is larger than mid
            left = mid + 1
        else:
            # missing interger is smaller than or equal mid
            right = mid

    if arr[left] != left:
        return left
    else:
        return right

print find_missing_number([0,1,2,3])





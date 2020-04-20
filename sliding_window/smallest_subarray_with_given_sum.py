'''
Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number.
'''

def getShortestSubArray(input_arr, k):
    shortest_length = -1
    left_side = 0
    right_side = 0
    cur_sum = input_arr[0]
    while right_side < len(input_arr):
        if left_side > right_side:
            right_side += 1
            if right_side == len(input_arr):
                break
            cur_sum += input_arr[right_side]
        elif cur_sum > k:
            cur_sum -= input_arr[left_side]
            left_side += 1
        elif cur_sum < k:
            right_side += 1
            if right_side == len(input_arr):
                break
            cur_sum += input_arr[right_side]
        else:
            cur_length = right_side - left_side + 1
            if shortest_length == -1:
                shortest_length = cur_length 
            elif shortest_length > cur_length:
                shortest_length = cur_length
            cur_sum -= input_arr[left_side]
            left_side += 1

    return shortest_length


if __name__ == '__main__':
    test_arr = [2,1,2]
    print getShortestSubArray(test_arr, 33)
    test_arr = [1, 4, 20, 3, 10, 5]
    print getShortestSubArray(test_arr, 33)
    test_arr = [1, 4, 0, 0, 3, 10, 5]
    print getShortestSubArray(test_arr, 7)

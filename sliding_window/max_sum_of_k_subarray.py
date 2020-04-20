'''
Given an array of size n, for each k from 1 to n, find the maximum sum of contiguous subarray of size k.
'''

def get_max_sum_subarray(k, input_arr):
    # calculate current sum
    cur_sum = 0
    for i in input_arr[:k]:
        cur_sum += i
    max_sum = cur_sum
    
    left_side = 0
    right_side = k-1
    while right_side+1 <= len(input_arr)-1:
        right_side += 1
        cur_sum += input_arr[right_side]
        cur_sum -= input_arr[left_side]
        left_side += 1
        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum

if __name__ == '__main__':
    test_input = [1, 2, 3, 4, 5]
    test_k = 3
    print get_max_sum_subarray(test_k, test_input)


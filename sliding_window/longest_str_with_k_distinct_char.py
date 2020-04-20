'''
Longest Substring Which contains K Unique Characters
'''

def getLongestSubString(input_str):
    # Use a hashmap to store the index of each character, if finding duplicate the left side of window will start from there
    left_side = 0
    right_side = 0
    max_length = 1
    max_left = 0
    max_right = 0
    
    char_cache = {}
    char_cache[input_str[0]] = 0

    while right_side + 1 <= len(input_str) - 1:
        right_side += 1
        if input_str[right_side] in char_cache:
            # clear all the other cache
            last_appear_index = char_cache[input_str[right_side]] + 1
            for i in input_str[left_side:last_appear_index]:
                del char_cache[i]
            char_cache[input_str[right_side]] = right_side
            left_side = last_appear_index
        else:
            char_cache[input_str[right_side]] = right_side
            cur_length = right_side - left_side
            if cur_length > max_length:
                max_length = cur_length
                max_left = left_side
                max_right = right_side - 1

    return max_length, max_left, max_right

def getLongestSubStringWithKUnique(input_str, k):
    # stores the last appear index
    char_cache = {}
    left_side = 0
    right_side = 0
    max_length = 0
    max_left = 0
    max_right = 0
    char_cache[input_str[0]] = 0
    
    while right_side + 1 <= len(input_str) - 1:
        right_side += 1
        cur_char = input_str[right_side]
        if cur_char in char_cache:
            char_cache[cur_char] = right_side
        else:
            if len(char_cache) == k:
                # find the smallest last appear index
                smallest_c = None
                smallest_index = right_side
                for c in char_cache:
                    if char_cache[c] < smallest_index:
                        smallest_index = char_cache[c]
                        smallest_c = c
                del char_cache[smallest_c]
                left_side = smallest_index + 1

            char_cache[cur_char] = right_side
            print left_side, right_side
        
        if len(char_cache) == k:
            cur_length = right_side - left_side + 1
            if max_length < cur_length:
                max_length = cur_length
                max_left = left_side
                max_right = right_side

    return max_length, input_str[max_left:max_right+1]

if __name__ == '__main__':
    test_input = "abbbbcacdefaghi"
    test_input = "abcadcacacaca"
    #print getLongestSubString(test_input)

    print getLongestSubStringWithKUnique(test_input, 3)

def find_sorted_messages(messages, interval):
    min_time, max_time = interval

    def bs_first_larger(messages, time):
        left = 0
        right = len(messages) - 1
        result = -1
        while left <= right:
            middle = left + (right - left) // 2
            if messages[middle] <= time:
                left = middle + 1
            else:
                result = middle
                right = middle - 1
        return result

    def bs_last_smaller(messages, time):
        left = 0
        right = len(messages) - 1
        result = -1
        while left <= right:
            middle = left + (right - left) // 2
            if messages[middle] >= time:
                right = middle - 1
            else:
                result = middle
                left = middle + 1
        return result

    left_bound = max(0, bs_first_larger(messages, min_time))
    right_bound = bs_last_smaller(messages, max_time)
    return messages[left_bound:right_bound+1]


print(find_sorted_messages([1,2,3,4,5,6,7,8,9,15,20, 33, 50, 51, 55, 99], (-2, 2)))


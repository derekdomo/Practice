def shuffle(arr):
    start = 2
    i = 2
    count  = 0
    cur = arr[i-1]
    while True:
        j = index(i, len(arr))
        arr[j-1], cur = cur, arr[j-1]
        i = j
        count += 1
        if count == len(arr) - 3:
            break
        if i == start:
            i = i + 2 
            cur = arr[i-1]
            start = i + 2
    print arr

def index(i, length):
    if i > length/2:
        i = (i - length/2)*2
    else:
        i = i*2 - 1 
    return i

shuffle([1,2,3,4,'a', 'b', 'c', 'd'])

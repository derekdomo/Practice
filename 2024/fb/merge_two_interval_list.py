def merge_two_interval_list(listA, listB):
    i = 0
    j = 0
    res = []
    while i < len(listA) or j < len(listB):
        if i == len(listA):
            res.append(listB[j])
            j += 1
        elif j == len(listB):
            res.append(listA[i])
            i += 1
        else:
            a = listA[i]
            b = listB[j]
            if a[1] < b[0]:
                res.append(a)
                i += 1
            elif a[0] > b[1]:
                res.append(b)
                j += 1
            elif a[1] >= b[1]:
                listA[i] = [min(a[0], b[0]), a[1]]
                j += 1
            else:
                listB[j] = [min(a[0], b[0]), b[1]]
                i += 1
    return res

A = [[1,5],[10,14],[16,18]]
B = [[2,6],[8,10],[11,20]]
print(merge_two_interval_list(A, B))

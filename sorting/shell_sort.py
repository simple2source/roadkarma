# shell sort
# 时间复杂度:  最优时间复杂度O(n^1.3)
#             最坏时间复杂度O(n^2)
#             平均时间复杂度O(nlogn) ~ O(n^2)
#             稳定性:不稳定
#             不需要额外空间 O(1)


def shell_sort(alist):
    length = len(alist)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            j = i
            while j >= gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        gap = gap // 2
    return alist


# test
l1 = [3, 2, 1, 0, 7, 11, 56, 23]
l2 = [8, 4, 1, 8, 4, 9, 3, 2]
print(shell_sort(l1))
print(shell_sort(l2))


def gap_insertion_sort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        current_value = alist[i]
        j = i
        while j >= gap and alist[j-gap] > current_value:
            alist[j] = alist[j-gap]
            j = j - gap
        alist[j] = current_value


def shell_sort2(alist):
    gap = len(alist) // 2
    while gap > 0:
        for i in range(gap):
            gap_insertion_sort(alist, i, gap)

        gap = gap // 2
    return alist


# test
l3 = [3, 2, 1, 0, 7, 11, 56, 23]
l4 = [8, 4, 1, 8, 4, 9, 3, 2]
print(shell_sort2(l3))
print(shell_sort2(l4))
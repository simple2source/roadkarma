# select sort
# 时间复杂度:  最优时间复杂度O(n^2)
#             最坏时间复杂度O(n^2)
#             平均时间复杂度O(n^2)
#             稳定性:不稳定
#             不需要额外空间


def selection_sort(alist):
    # use the max to select
    length = len(alist)
    for i in range(length - 1, 0, -1):
        max_index = 0
        for j in range(1, i + 1):
            if alist[j] > alist[max_index]:
                max_index = j
        alist[i], alist[max_index] = alist[max_index], alist[i]
    return alist


# test
l1 = [3, 2, 1, 0, 7, 11, 56, 23]
l2 = [8, 4, 1, 8, 4, 9, 3, 2]
print(selection_sort(l1))
print(selection_sort(l2))


def selection_sort_2(alist):
    # use the min to select
    length = len(alist)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i], alist[min_index] = alist[min_index], alist[i]
    return alist


# test
l3 = [3, 2, 1, 0, 7, 11, 56, 23]
l4 = [8, 4, 1, 8, 4, 9, 3, 2]
print(selection_sort_2(l3))
print(selection_sort_2(l4))

# 选择排序优化，2元选择排序


def selection_sort_3(alist):
    length = len(alist)
    for i in range(length//2):
        min_index, max_index = i, i
        for j in range(i, length-i):
            if alist[j] < alist[min_index]:
                min_index = j
                continue
            if alist[j] > alist[max_index]:
                max_index = j
        alist[min_index], alist[i] = alist[i], alist[min_index]
        alist[max_index], alist[length - i - 1] = alist[length - i - 1], alist[max_index]
        # if min_index != i:
        #     alist[min_index], alist[i] = alist[i], alist[min_index]
        # if max_index != length-i-1:
        #     alist[max_index], alist[length-i-1] = alist[length-i-1], alist[max_index]
    return alist


def selection_sort_4(alist):
    length = len(alist)
    for i in range(length//2):
        min_index, max_index = i, i
        for j in range(i, length-i):
            if alist[j] < alist[min_index]:
                min_index = j
                continue
            if alist[j] > alist[max_index]:
                max_index = j
        alist[min_index], alist[i] = alist[i], alist[min_index]
        if max_index == i:
            alist[max_index], alist[length - i - 1] = alist[length - i - 1], alist[min_index]
        else:
            alist[max_index], alist[length - i - 1] = alist[length - i - 1], alist[max_index]
        # if min_index != i:
        #     alist[min_index], alist[i] = alist[i], alist[min_index]
        # if max_index != length-i-1:
        #     alist[max_index], alist[length-i-1] = alist[length-i-1], alist[max_index]
    return alist


# test
l5 = [3, 2, 1, 0, 7, 11, 56, 23]
l6 = [8, 4, 1, 8, 4, 9, 3, 2]
l7 = [8, 3, 4]
print(selection_sort_4(l5))
print(selection_sort_4(l7))


def selection_sort_5(alist):
    length = len(alist)

    for i in range(length//2):
        max_index = i
        min_index = -i - 1
        min_origin = min_index
        for j in range(i+1, length-i):
            if alist[max_index] < alist[j]:
                max_index = j
            if alist[min_index] > alist[-j -1]:
                min_index = -j - 1
        if alist[max_index] == alist[min_index]:
            break

        if i != max_index:
            tmp = alist[i]
            alist[i] = alist[max_index]
            alist[max_index] = tmp

            if i == min_index or i == length + min_index:
                min_index = max_index

        if min_origin != min_index and alist[min_origin] != alist[min_index]:
            tmp = alist[min_origin]
            alist[min_origin] = alist[min_index]
            alist[min_index] = tmp

    return alist


# test
l8 = [3, 2, 1, 0, 7, 11, 56, 23]
l9 = [8, 4, 1, 8, 4, 9, 3, 2]
l10 = [ 3, 4,7]
print(selection_sort_5(l9))
print(selection_sort_5(l10))

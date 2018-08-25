# bubble sort
# https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php
#
# 时间复杂度:  最优时间复杂度O(n) 当遍历一次的时候发现没有任何元素交换，说明已经是按大小有序的，排序结束
#             最坏时间复杂度O(n^2)
#             平均时间复杂度O(n^2)
#             稳定性:稳定
#             不需要额外空间


def bubble_sort(alist):
    """

    :param alist:
    :return:
    """
    length = len(alist)
    n = 0
    n2 = 0
    for i in range(length):
        for j in range(i):
            n += 1
            if alist[j] > alist[i]:
                n2 += 1
                alist[i], alist[j] = alist[j], alist[i]
    return alist, n, n2


def bubble_sort_2(alist):
    length = len(alist)
    n = 0
    n2 = 0
    for i in range(length):
        for j in range(i + 1, length):
            n += 1
            if alist[i] > alist[j]:
                n2 += 1
                alist[i], alist[j] = alist[j], alist[i]
    return alist, n, n2


def bubble_sort_3(alist):
    length = len(alist)
    n = 0
    n2 = 0
    for i in range(length - 1, 0, -1):
        for j in range(i):
            n += 1
            if alist[j] > alist[j + 1]:
                n2 += 1
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist, n, n2


def short_bubble_sort(alist):
    exchange = True
    length = len(alist) - 1
    while length > 0 and exchange:
        exchange = False
        for i in range(length):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        length = length - 1
    return alist


# test
print(bubble_sort([3, 5, 6, 2, 1, 3, 1, 7, 12]))
print(bubble_sort([8, 4, 1, 8, 4, 9, 3, 2]))
print(bubble_sort([6, 5, 4, 3, 2]))

print(bubble_sort_2([3, 5, 6, 2, 1, 3, 1, 7, 12]))
print(bubble_sort_2([8, 4, 1, 8, 4, 9, 3, 2]))
print(bubble_sort_2([6, 5, 4, 3, 2]))

print(bubble_sort_3([3, 5, 6, 2, 1, 3, 1, 7, 12]))
print(bubble_sort_3([8, 4, 1, 8, 4, 9, 3, 2]))
print(bubble_sort_3([6, 5, 4, 3, 2]))

# quick sort
# 时间复杂度:  最优时间复杂度O(nlogn)
#             最坏时间复杂度O(n^2)
#             平均时间复杂度O(nlogn)
#             稳定性:不稳定
#             不需要额外空间
#             优化：1、当数组为升序或者降序的时候，将基准值进行改变（随便选择基准值来进行比较）

from random import randrange


def quick_sort(alist, first, last):
    if first >= last:
        return
    mid = alist[first]
    left = first
    right = last

    while left < right:
        while left < right and alist[right] >= mid:
            right -= 1
        alist[left] = alist[right]

        while left < right and alist[left] < mid:
            left += 1
        alist[right] = alist[left]
    alist[left] = mid

    quick_sort(alist, first, left - 1)
    quick_sort(alist, left + 1, last)
    return alist


# test
l1 = [3, 2, 1, 0, 7, 11, 56, 23]
l2 = [8, 4, 1, 8, 4, 9, 3, 2]
print(quick_sort(l1, 0, len(l1) - 1))
print(quick_sort(l2, 0, len(l2) - 1))


def quick_sort2(alist):
    if len(alist) < 2:
        return alist
    else:
        pivot_value = alist[0]
        less = [i for i in alist[1:] if i <= pivot_value]
        greater = [i for i in alist[1:] if i > pivot_value]
        return quick_sort2(less) + [pivot_value] + quick_sort2(greater)


# test
l3 = [3, 2, 1, 0, 7, 11, 56, 23]
l4 = [8, 4, 1, 8, 4, 9, 3, 2]
print(quick_sort2(l3))
print(quick_sort2(l4))


def partition(lst, start, end, pivot):
    lst[pivot], lst[end] = lst[end], lst[pivot]
    store_index = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[store_index] = lst[store_index], lst[i]
            store_index += 1
    lst[store_index], lst[end] = lst[end], lst[store_index]
    return store_index


def quick_sort3(alist, first, last):
    if first >= last:
        return
    pivot = randrange(first, last + 1)
    new_pivot = partition(alist, first, last, pivot)
    quick_sort3(alist, first, new_pivot - 1)
    quick_sort3(alist, new_pivot + 1, last)
    return alist


# test
l5 = [3, 2, 1, 0, 7, 11, 56, 23]
l6 = [8, 4, 1, 8, 4, 9, 3, 2]

print(quick_sort3(l5, 0, len(l5) - 1))
print(quick_sort3(l6, 0, len(l6) - 1))


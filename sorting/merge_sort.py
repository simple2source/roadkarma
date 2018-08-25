# merge sort
# 时间复杂度:  最优时间复杂度O(nlogn)
#             最坏时间复杂度O(nlogn)
#             平均时间复杂度O(nlogn)
#             稳定性:稳定
#             需要额外空间:O(n)


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[:mid]
        right_half = alist[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i = i + 1
            else:
                alist[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j = j + 1
            k = k + 1
    return alist


# test
l1 = [3, 2, 1, 0, 7, 11, 56, 23]
l2 = [8, 4, 1, 8, 4, 9, 3, 2]
print(merge_sort(l1))
print(merge_sort(l2))


def merge2(left, right):
    """
    # 对已经排序好的2个list进行合并
    :param left: sorted
    :param right: sorted
    :return:
    """
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


def merge_sort2(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left = merge_sort2(alist[:mid])
    right = merge_sort2(alist[mid:])

    return merge2(left, right)


# test
l3 = [3, 2, 1, 0, 7, 11, 56, 23]
l4 = [8, 4, 1, 8, 4, 9, 3, 2]
print(merge_sort2(l3))
print(merge_sort2(l4))


def merge3(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.remove(left[0])
        else:
            result.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        result += right
    else:
        result += left
    return result


def merge_sort3(alist):
    if len(alist) <= 1:
        return alist

    mid = len(alist) // 2
    left = merge_sort3(alist[:mid])
    right = merge_sort3(alist[mid:])
    return merge3(left, right)


# test
l5 = [3, 2, 1, 0, 7, 11, 56, 23]
l6 = [8, 4, 1, 8, 4, 9, 3, 2]
print(merge_sort3(l5))
print(merge_sort3(l6))

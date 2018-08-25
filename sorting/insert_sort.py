# insert sort
# 时间复杂度:  最优时间复杂度O(n) 已经是升序的
#             最坏时间复杂度O(n^2) 也是平均时间复杂度
#             平均时间复杂度O(n^2)
#             稳定性:稳定
#             不需要额外空间


def insert_sort(alist):
    length = len(alist)
    count = 0
    for i in range(length):
        j = i
        while j > 0:
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
                count += 1
            j -= 1
    print(count, 'errr')

    return alist


# test
print(insert_sort([3, 2, 1, 0, 7, 11, 56, 23]))


# print(insert_sort([1, 2, 3, 32, 5, 7, 99, 77]))


def insert_sort2(alist):
    length = len(alist)
    for i in range(1, length):
        current_value = alist[i]
        j = i
        while j > 0 and alist[j - 1] > current_value:
            alist[j] = alist[j - 1]
            j = j - 1
        alist[j] = current_value


# test
print(insert_sort([3, 2, 1, 0, 7, 11, 56, 23]))


def insertion_sort(array):
    for i in range(len(array)):
        current_value = array[i]
        j = i
        while j > 0 and array[j - 1] > current_value:
            array[j] = array[j - 1]
            j = j - 1
        array[j] = current_value
        print(current_value, 'why', j, array)
    return array


# test
print(insertion_sort([3, 2, 1, 0, 7, 11, 56, 23]))

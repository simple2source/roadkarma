# leetcode 53:Maximum Subarray
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6.


def max_sub_array_sum(array):
    if not array:
        return None
    max_num = 0
    sum_num = 0
    length = len(array)
    for i in range(length):
        if sum_num < 0:
            sum_num = 0
        sum_num += array[i]
        max_num = max(max_num, sum_num)
    return max_num


# test
print(max_sub_array_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# 不能计算出负数的情况
print(max_sub_array_sum([-4, -1, -2, -4, - 9]))


def max_sub_array_sum_2(array):
    length = len(array)
    max_so_far = array[0]
    current_max = array[0]
    for i in range(1, length):
        current_max = max(array[i], current_max + array[i])
        max_so_far = max(max_so_far, current_max)
    return max_so_far


# test
print(max_sub_array_sum_2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sub_array_sum_2([-4, -11, -3, -5, -4, -9]))
print(max_sub_array_sum_2([5, 2, 1, 6, 8, 0, -2, 5]), '-------')


def max_sub_array_sum_and_index(array):
    length = len(array)
    max_so_far = 0
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(length):
        max_ending_here += array[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
    return max_so_far, start, end


# test
print(max_sub_array_sum_and_index([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sub_array_sum_and_index([-4, -11, -3, -5, -4, -9]))

if __name__ == '__main__':
    pass

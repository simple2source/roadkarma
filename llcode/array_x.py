
def find_idx(L):
    idx = len(L) -1
    max_s = float('-inf')
    s = 0
    for i in range(idx, -1, -1):
        s += L[i]
        if s > max_s:
            idx = i
            max_s = s
    print(idx, '---')
    return idx

find_idx([1,2,3,-1,2,6,5])
find_idx([1,2,5,-8,4,6,-9,-11])
# l = [1, 4, -5, 3, 7, 11, -9] , 55:Maximum Subarray

def find_iadd_max_num_index(array):
    if not array:
        return None
    length = len(array)
    l = []
    max_num = 0
    for i in range(0, length):
        if array[i]>0:
            max_num+=array[i]
        else:
            l.append((max_num, i))
            max_num = 0
    else:
        if max_num>0:
            l.append((max_num, i))

    max_num = 0
    idx = 0
    for it in l:
        if it[0]>max_num:
            max_num,idx = it
    print(max_num, idx)

if __name__ == '__main__':
    find_iadd_max_num_index([1, 4, -5, 6, 7, 11, -9, 12, 45, -4, 11])
    find_iadd_max_num_index([1, 4, -5, 3, 7, 11, -9])
    find_iadd_max_num_index([-1,-2, -3, 2, 5,4])
    find_iadd_max_num_index([1,2,3,-1,2,6,5])

def mp_sort(l):
    length = len(l)
    print(length)
    for i in range(length):
        print(i)
        for j in range(i+1, length):
            if l[i] > l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
    print(l)

if __name__ == '__main__':
    mp_sort([4, 2, 3, 6, 4, 7, 3, 2])
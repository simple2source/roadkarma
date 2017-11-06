#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# -------------- chapter-1
"""
binary search
https://stackoverflow.com/questions/212358/binary-search-bisection-in-python
"""


# method-1
def binary_search(a, l, low=0, high=None):
    if high is None:
        high = len(l)
    while low < high:
        mid = (high + low)//2
        mid_value = l[mid]
        if a > mid_value:
            low = mid + 1
        elif a < mid_value:
            high = mid
        else:
            return 0
    return -1


# method-2 recurse
# https://codereview.stackexchange.com/questions/102705/recursive-binary-search-in-python
def binary_search_recurse(a, l, low=0, high=None):
    if high is None:
        high = len(l)
    mid = (high + low)//2
    if low >= high:
        print(-1)
        return -1
    mid_value = l[mid]
    if a > mid_value:
        low = mid + 1
        return binary_search_recurse(a, l, low, high)
    elif a < mid_value:
        high = mid - 1
        return binary_search_recurse(a, l, low, high)
    else:
        print(0)
        return 0

# ------------- chapter-1 end


# ------------- chapter-2

"""
list directory all file
https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
os.walk ======> top_dir,dir_list,file_list

"""

# error implement
# 递归调用的时候，当一个目录下有多个目录的时候，
# 只会将一个目录传入到其中，其他的目录不会调用函数,所以多个目录的时候，其他文件遗漏
files = []


def list_file(directory):
    for path in os.listdir(os.path.abspath(directory)):
        if os.path.isfile(os.path.join(os.path.abspath(directory), path)):
            print('path file', path)
            files.append(path)
    dirs = []
    for path in os.listdir(os.path.abspath(directory)):
        if os.path.isdir(os.path.join(os.path.abspath(directory), path)):
            real_path = os.path.join(os.path.abspath(directory), path)
            dirs.append(real_path)
            print('real_path', real_path)
    for path in dirs:
        return list_file(path)


# method-1 last answer :
# https://stackoverflow.com/questions/18394147/recursive-sub-folder-search-and-return-files-in-a-list-python
def search_files(files_, dirs):
    """
    :param files_: -> list
    :param dirs:   -> list
    :return:
    """
    new_dirs = []
    for d in dirs:
        for f in os.listdir(d):
            if os.path.isdir(os.path.join(d, f)):
                new_dirs.append(os.path.join(d, f))
            else:
                files_.append(os.path.join(d, f))
    if new_dirs:
        return search_files(files_, new_dirs)
    else:
        print(files_)
        return files_

if __name__ == '__main__':
    binary_search_recurse(5, [1, 2, 3, 4])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

单链表python implement,并且逆序

# 参考资料
https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
http://www.geeksforgeeks.org/reverse-a-linked-list/
"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        while current:
            if current.get_data() == data:
                print('found')
                return current
            current = current.get_next()
        raise ValueError('not found data in linkedlist')

    # method-1 self implement
    def delete_1(self, data):
        current = self.head
        if current.get_data() == data:
            self.head = self.head.get_next()
            return True
        while current:
            next_node = current.get_next()
            if next_node.get_data() == data:
                current.set_next(next_node.get_next())
                next_node.set_next(None)
                return True
            current = next_node
        raise ValueError('{} not in list'.format(data))

    # method-2
    def delete_2(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError('data not in list')
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    # method-1 iter
    def reversed_iter(self):
        last = None
        current = self.head
        while current:
            next_node = current.get_next()
            current.set_next(last)
            last = current
            current = next_node
        self.head = last

    # method-2 recurse
    def reversed_recurse_2(self, head, last_node):
        if head is None:
            self.head = last_node
            return last_node
        next_node = head.next_node
        head.next_node = last_node
        last_node = head
        return self.reversed_recurse_2(next_node, last_node)

    def reversed_list_recurse(self):
        return self.reversed_recurse_2(self.head, None)

    def print_all(self):
        current = self.head
        while current:
            print(current.get_data())
            current = current.get_next()

if __name__ == '__main__':
    s = LinkedList()
    for x in range(7):
        s.insert(x)
    s.delete_2(4)
    s.print_all()

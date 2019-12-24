# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
from heapq import heapify, heappop, heappush, heappushpop

class PriorityQueue:
    def __init__(self, heap):
        '''
        heap ... list
        '''
        self.heap = heap
        heapify(self.heap)

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)

    def pushpop(self, item):
        return heappushpop(self.heap, item)

    def __call__(self):
        return self.heap

    def __len__(self):
        return len(self.heap)
    
    def __repr__(self):
        return str(self.heap)


# -

class Obj(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return '({0}, {1})'.format(self.x, self.y)
    def __lt__(self, obj):
        return (self.x**2 + self.y**2) < (obj.x**2 + obj.y**2)

# +
# a = Obj(2, 3)
# b = Obj(1, 5)
# c = Obj(3, 0)
# d = Obj(0, 0)
# e = Obj(5, 6)
# f = Obj(6, 5)
# q1 = PriorityQueue([])
# q1.push(a)
# q1.push(b)
# q1.push(c)
# q1.push(d)
# q1.push(e)
# q1.push(f)
# q1

# +
# print(q1.pop())
# print(q1.pop())
# print(q1.pop())
# print(q1.pop())
# print(q1.pop())
# print(q1.pop())

# +
# q2 = PriorityQueue([])
# a = 'abc'
# b = 'aaedd'
# c = 'daa'
# d = 'a'
# q2.push(a)
# q2.push(b)
# q2.push(c)
# q2.push(d)
# q2

# +
# print(q2.pop())
# print(q2.pop())
# print(q2.pop())
# print(q2.pop())
# -



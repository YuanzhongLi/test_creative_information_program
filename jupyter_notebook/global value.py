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

a = 0
def f1():
    global a
    a += 1
a    

f1()
a


def f2():
    def local():
        global a
        a += 1
    local()    


a

f2()
a


def f3():
    f1()


a

f3()
a



# -*- coding: utf-8 -*-
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

# (1)
file_path = 'prog1.txt'
def solve(file_path):
    with open(file_path, encoding='ascii') as f:
        line1 = f.readline()
        code_array = line1.split(' ')
        order = code_array[0]
        operand1 = code_array[1]
        operand2 = code_array[2]    
        print(operand1)


solve(file_path)

# +
# (2)
y = 0
x = 1
while (x != 10):
    y += x
    x += 1
        
print(x, y)

# +
# (3)
import sys
sys.path.append('..')
import IsStrNumber as isn

file_path = 'prog2.txt'
def solve(file_path):
    max_order = 100
    orders = [] 
    register = { 'x': 0, 'y': 0 }
    with open(file_path, encoding='ascii') as f:
        for i in range(0, max_order):
            line = f.readline()
            if (line != ''):
                line = line.rstrip('\n')
                code_array = line.split(' ')
                orders.append(code_array)
                
    def compileOrder(order, op1, op2):
        if (order == 'ADD'):
            if (isn.isNumber(op1)):
                register[op2] += isn.STRtoNumber(op1)
            else:
                register[op2] += register[op1]
        elif (order == 'PRN'):
            if (isn.isNumber(op1)):
                if (isn.isNumber(op2)):
                    print(isn.STRtoNumber(op1), isn.STRtoNumber(op2))
                else:
                    print(isn.STRtoNumber(op1), register[op2])
            else:
                if (isn.isNumber(op2)):
                    print(register[op1], isn.STRtoNumber(op2))
                else:
                    print(register[op1], register[op2])
                    
        elif (order == 'SET'):
            if (isn.isNumber(op2)):
                register[op1] = isn.STRtoNumber(op2)
            else:
                register[op1] = register[op2]
    for i in range(0, len(orders)):
        order = orders[i][0]
        op1 = orders[i][1]
        op2 = orders[i][2]        
        compileOrder(order, op1, op2)


# -

solve(file_path)

# +
# (4)
import sys
sys.path.append('..')
import IsStrNumber as isn

file_path = 'prog3.txt'
def solve(file_path):
    max_order = 100
    orders = [] 
    register = {}
    with open(file_path, encoding='ascii') as f:
        for i in range(0, max_order):
            line = f.readline()
            if (line != ''):
                line = line.rstrip('\n')
                code_array = line.split(' ')
                orders.append(code_array)
    
    # python のglobal変数が使い辛すぎるのでこうした
    next_order = { 'num': 0 }        
    
    def compileOrder(order, op1, op2):
        if (order == 'ADD'):
            next_order['num'] += 1                    
            if (isn.isNumber(op1)):
                register[op2] += isn.STRtoNumber(op1)
            else:
                register[op2] += register[op1]
        elif (order == 'PRN'):
            next_order['num'] += 1            
            if (isn.isNumber(op1)):
                if (isn.isNumber(op2)):
                    print(isn.STRtoNumber(op1), isn.STRtoNumber(op2))
                else:
                    print(isn.STRtoNumber(op1), register[op2])
            else:
                print(register[op1], register[op2])
        elif (order == 'SET'):
            next_order['num'] += 1                    
            if (isn.isNumber(op2)):
                register[op1] = isn.STRtoNumber(op2)
            else:
                register[op1] = register[op2]
        elif (order == 'CMP'):
            next_order['num'] += 1                    
            if (isn.isNumber(op1)):
                if (isn.isNumber(op2)):
                    if (isn.STRtoNumber(op1) == isn.STRtoNumber(op2)):
                        next_order['num'] += 1
                else:
                    if (isn.STRtoNumber(op1) == register[op2]):
                        next_order['num'] += 1                        
            else:
                if (isn.isNumber(op2)):
                    if (register[op1] == isn.STRtoNumber(op2)):
                        next_order['num'] += 1                        
                else:
                    if (register[op1] == register[op2]):
                        next_order['num'] += 1                        
        elif (order == 'JMP'):
            if (isn.isNumber(op1)):
                next_order['num'] += isn.STRtoNumber(op1)
            else:
                next_order['num'] += register[op1]            
    
    while (next_order['num'] < len(orders)):
        order = orders[next_order['num']][0]
        op1 = orders[next_order['num']][1]
        op2 = orders[next_order['num']][2]
#         print(order, op1, op2)
        compileOrder(order, op1, op2)


# -

solve(file_path)

# +
# (5)
import sys
sys.path.append('..')
import IsStrNumber as isn

file_path = 'prog4.txt'
def solve(file_path):
    max_order = 100
    orders = [] 
    register = {}
    with open(file_path, encoding='ascii') as f:
        for i in range(0, max_order):
            line = f.readline()
            if (line != ''):
                line = line.rstrip('\n')
                code_array = line.split(' ')
                orders.append(code_array)
    
    # python のglobal変数が使い辛すぎるのでこうした
    next_order = { 'num': 0 } 
    sub_order_stack = []    
    
    def compileOrder(order, op1, op2):
        if (order == 'ADD'):
            next_order['num'] += 1                    
            if (isn.isNumber(op1)):
                register[op2] += isn.STRtoNumber(op1)
            else:
                register[op2] += register[op1]
        elif (order == 'PRN'):
            next_order['num'] += 1            
            if (isn.isNumber(op1)):
                if (isn.isNumber(op2)):
                    print(isn.STRtoNumber(op1), isn.STRtoNumber(op2))
                else:
                    print(isn.STRtoNumber(op1), register[op2])
            else:
                print(register[op1], register[op2])
        elif (order == 'SET'):
            next_order['num'] += 1                    
            if (isn.isNumber(op2)):
                register[op1] = isn.STRtoNumber(op2)
            else:
                register[op1] = register[op2]
        elif (order == 'CMP'):
            next_order['num'] += 1                    
            if (isn.isNumber(op1)):
                if (isn.isNumber(op2)):
                    if (isn.STRtoNumber(op1) == isn.STRtoNumber(op2)):
                        next_order['num'] += 1
                else:
                    if (isn.STRtoNumber(op1) == register[op2]):
                        next_order['num'] += 1                        
            else:
                if (isn.isNumber(op2)):
                    if (register[op1] == isn.STRtoNumber(op2)):
                        next_order['num'] += 1                        
                else:
                    if (register[op1] == register[op2]):
                        next_order['num'] += 1                        
        elif (order == 'JMP'):
            if (isn.isNumber(op1)):
                next_order['num'] += isn.STRtoNumber(op1)
            else:
                next_order['num'] += register[op1]
        elif (order == 'SUB'):
            # 次のorderをstackに保存
            sub_order_stack.append(next_order['num']+1)
            compileOrder('JMP', op1, op2)             
        elif(order == 'BAK'):
            next_order['num'] = sub_order_stack.pop()
    
    while (next_order['num'] < len(orders)):
        order = orders[next_order['num']][0]
        op1 = orders[next_order['num']][1]
        op2 = orders[next_order['num']][2]
#         print(order, op1, op2)
        compileOrder(order, op1, op2)


# -

solve(file_path)

# +
# (6)
import sys
sys.path.append('..')
import IsStrNumber as isn

file_path = 'prog3.txt'
def solve(file_path):
    max_order = 100
    orders = [] 
    with open(file_path, encoding='ascii') as f:
        for i in range(0, max_order):
            line = f.readline()
            if (line != ''):
                line = line.rstrip('\n')
                code_array = line.split(' ')
                orders.append(code_array)
    
    # python のglobal変数が使い辛すぎるのでこうした
    next_order = { 'num': 0 } 
    sub_order_stack = []   
    
    # register_stack[0]をglobal register(実際のレジスタ)とする
    register_stack = [{}]
    # register_stackの最後尾のregisterオブジェクトを使用することによって局所レジスタを実現
    
    def compileOrder(order, op1, op2):
        if (order == 'ADD'):
            next_order['num'] += 1                    
            if (isn.isNumber(op1)):
                register_stack[len(register_stack)-1][op2] += isn.STRtoNumber(op1)
            else:
                register_stack[len(register_stack)-1][op2] += register_stack[len(register_stack)-1][op1]
        elif (order == 'PRN'):
            next_order['num'] += 1            
            if (isn.isNumber(op1)):
                if (isn.isNumber(op2)):
                    print(isn.STRtoNumber(op1), isn.STRtoNumber(op2))
                else:
                    print(isn.STRtoNumber(op1), register_stack[len(register_stack)-1][op2])
            else:
                print(register_stack[len(register_stack)-1][op1], register_stack[len(register_stack)-1][op2])
        elif (order == 'SET'):
            next_order['num'] += 1                    
            if (isn.isNumber(op2)):
                register_stack[len(register_stack)-1][op1] = isn.STRtoNumber(op2)
            else:
                register_stack[len(register_stack)-1][op1] = register_stack[len(register_stack)-1][op2]
        elif (order == 'CMP'):
            next_order['num'] += 1                    
            if (isn.isNumber(op1)):
                if (isn.isNumber(op2)):
                    if (isn.STRtoNumber(op1) == isn.STRtoNumber(op2)):
                        next_order['num'] += 1
                else:
                    if (isn.STRtoNumber(op1) == register_stack[len(register_stack)-1][op2]):
                        next_order['num'] += 1                        
            else:
                if (isn.isNumber(op2)):
                    if (register_stack[len(register_stack)-1][op1] == isn.STRtoNumber(op2)):
                        next_order['num'] += 1                        
                else:
                    if (register_stack[len(register_stack)-1][op1] == register_stack[len(register_stack)-1][op2]):
                        next_order['num'] += 1                        
        elif (order == 'JMP'):
            if (isn.isNumber(op1)):
                next_order['num'] += isn.STRtoNumber(op1)
            else:
                next_order['num'] += register_stack[len(register_stack)-1][op1]
        elif (order == 'SUB'):
            # 次のorderをstackに保存
            sub_order_stack.append(next_order['num']+1)
            compileOrder('JMP', op1, op2)             
        elif (order == 'BAK'):
            next_order['num'] = sub_order_stack.pop()
        elif (order == 'CAL'):
            sub_order_stack.append(next_order['num']+1)
            new_register = { 'in': 0 }
            if (isn.isNumber(op2)):
                new_register['in'] = isn.STRtoNumber(op2)
            else:
                new_register['in'] = register_stack[len(register_stack)-1][op2]
            compileOrder('JMP', op1, op2)
            # JMPしてから局所レジスタをスタックに追加
            register_stack.append(new_register)
        elif (order == 'RET'):
            next_order['num'] = sub_order_stack.pop()
            # 局所レジスタを消去
            old_register = register_stack.pop()
            # 局所を抜けた後にoutを使用できるように、抜けた直後の局所registerにoutを追加
            if (isn.isNumber(op1)):
                register_stack[len(register_stack)-1]['out'] = isn.STRtoNumber(op1)
            else:
                register_stack[len(register_stack)-1]['out'] = old_register[op1]
    
    while (next_order['num'] < len(orders)):
        order = orders[next_order['num']][0]
        op1 = orders[next_order['num']][1]
        op2 = orders[next_order['num']][2]
#         print(order, op1, op2)
        compileOrder(order, op1, op2)


# -

solve(file_path)

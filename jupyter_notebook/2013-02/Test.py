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

import sys
sys.path.append('..')

import numpy as np


# (1)
def solve1(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        if text[-1] == '\n':
            text = text[:-1]
        ret = text.split('+')
        return ret    
def print1(ret):
    for txt in ret:
        print(txt)


print1(solve1('test001.txt'))


# +
# (2)
def solve1(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        if text[-1] == '\n':
            text = text[:-1]
        ret = text.split('+')
        return ret 
    
def solve2(file_path):
    txts = solve1(file_path)
    al_set = set()
    groups = []
    for index, txt in enumerate(txts):
        als = txt.split('&')
        group = []
        for al in als:
            group.append(al)
            al_set.add(al)
        group.sort()
        groups.append(group) 
        
    al_set2 = []   
    for al in al_set:
        al_set2.append(al)
    al_set2.sort()    
    
    answers = set()
    for group in groups:
        ans = ['']
        for al in al_set2:
            if al in group:
                for i in range(len(ans)):
                    ans[i] += '{0}=true '.format(al)
#                     print(ans)
            else:
                tmp = len(ans)
                ans = ans * 2
                for i in range(tmp):
                    ans[i] += '{0}=true '.format(al)
                    ans[i+tmp] += '{0}=false '.format(al)
        for txt in ans:
            answers.add(txt)
    if len(answers) > 0:
        for a in answers:
            print(a)
    else:
        print('none')


# -

solve2('test001.txt')


# +
# (3)
def solve1(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        if text[-1] == '\n':
            text = text[:-1]
        ret = text.split('+')
        return ret

# a&!aが存在するかどうか  
# groupでは!aをa!の形で持っている
def isNone(group):
    for al in group:
        if (al+'!') in group:
            return True
    return False    
    
def solve3(file_path):
    txts = solve1(file_path)
    al_set = set()
    groups = []
    for index, txt in enumerate(txts):
        als = txt.split('&')
        group = []
        for al in als:
            last = al[-1]
            if (len(al) % 2) == 0:
                group.append(last+'!')
            else:
                group.append(last)
            al_set.add(last)
        group.sort()
        groups.append(group)    
        
    al_set2 = []   
    for al in al_set:
        al_set2.append(al)
    al_set2.sort()    
    
#     print(al_set2)
#     print(groups)
#     return
    
    answers = set()
    for group in groups:
        if not isNone(group):
            ans = ['']
            for al in al_set2:
                if al in group:
                    for i in range(len(ans)):
                        ans[i] += '{0}=true '.format(al)
                elif (al+'!') in group:
                    for i in range(len(ans)):
                        ans[i] += '{0}=false '.format(al)
                else:
                    tmp = len(ans)
                    ans = ans * 2
                    for i in range(tmp):
                        ans[i] += '{0}=true '.format(al)
                        ans[i+tmp] += '{0}=false '.format(al)
            for txt in ans:
                answers.add(txt)
    if len(answers) > 0:
        for a in answers:
            print(a)
    else:
        print('none')


# +
# solve3('test002.txt')

# +
# (4)
from N_DIGIT import baseNumbers

alpha = ['a', 'b', 'c', 'd', 'e', 
         'f', 'g', 'h', 'i', 'j', 
         'k', 'l', 'm', 'n', 'o',
         'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'x',
        ]
    
def get_alpha_set(text):
    ret = []
    for al in alpha:
        if al in text:
            ret.append(al)
    ret.sort()    
    return ret

def macro(text):
        text = text.replace('!', ' not ')
        text = text.replace('&', ' and ')
        text = text.replace('+', ' or ')
        return text       

def solve4(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        if text[-1] == '\n':
            text = text[:-1]
    al_set = get_alpha_set(text)
    al_dic = {}
    for index, al in enumerate(al_set):
        al_dic[al] = index
    bs = baseNumbers(1 << len(al_set), 2, len(al_set))
    ans = []
    for b in bs:
        tmp = text
        for al in al_set:
            tmp = tmp.replace(al, str(b[al_dic[al]]))
        formatted_tmp = macro(tmp)
        if eval(formatted_tmp):
            ans.append(b)
    for a in ans:
        txt = ''
        for index, boolean in enumerate(a):
            if boolean:
                al = al_set[index]
                txt += '{0}=true '.format(al)
            else:
                al = al_set[index]
                txt += '{0}=false '.format(al)
        print(txt)    


# +
# solve4('test002.txt')

# +
# (5)
from N_DIGIT import baseNumbers

alpha = ['a', 'b', 'c', 'd', 'e', 
         'f', 'g', 'h', 'i', 'j', 
         'k', 'l', 'm', 'n', 'o',
         'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'x',
        ]
    
def get_alpha_set(text):
    ret = []
    for al in alpha:
        if al in text:
            ret.append(al)
    ret.sort()    
    return ret

def macro(text):
        text = text.replace('!', ' not ')
        text = text.replace('&', ' and ')
        text = text.replace('+', ' or ')
        return text       

def solve5(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        if text[-1] == '\n':
            text = text[:-1]
    al_set = get_alpha_set(text)
    al_dic = {}
    for index, al in enumerate(al_set):
        al_dic[al] = index
    bs = baseNumbers(1 << len(al_set), 2, len(al_set))
    ans = []
    for b in bs:
        tmp = text
        for al in al_set:
            tmp = tmp.replace(al, str(b[al_dic[al]]))
        formatted_tmp = macro(tmp)
        if eval(formatted_tmp):
            ans.append(b)
            
    txt = ''
    for a in ans:
        tmp = ''
        for index, boolean in enumerate(a):
            if boolean:
                al = al_set[index]
                tmp += (al+'&')
            else:
                al = al_set[index]
                tmp += ('!'+al+'&')
        txt += (tmp[:-1]+'+')
    print(txt[:-1])



# -

solve5('test001.txt')

# +
# (6)
from N_DIGIT import baseNumbers

alpha = ['a', 'b', 'c', 'd', 'e', 
         'f', 'g', 'h', 'i', 'j', 
         'k', 'l', 'm', 'n', 'o',
         'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'x',
        ]
    
def get_alpha_set(text):
    ret = []
    for al in alpha:
        if al in text:
            ret.append(al)
    ret.sort()    
    return ret

def macro(text):
        text = text.replace('!', ' not ')
        text = text.replace('&', ' and ')
        text = text.replace('+', ' or ')
        return text       

def solve6(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        if text[-1] == '\n':
            text = text[:-1]
    al_set = get_alpha_set(text)
    al_dic = {}
    for index, al in enumerate(al_set):
        al_dic[al] = index
    bs = baseNumbers(1 << len(al_set), 2, len(al_set))
    ans = []
    for b in bs:
        tmp = text
        for al in al_set:
            tmp = tmp.replace(al, str(b[al_dic[al]]))
        formatted_tmp = macro(tmp)
        if not eval(formatted_tmp):
            ans.append(b)
            
    txt = ''
    for a in ans:
        tmp = '('
        for index, boolean in enumerate(a):
            if boolean:
                al = al_set[index]
                tmp += ('!'+al+'+')
            else:
                al = al_set[index]
                tmp += (al+'+')
        txt += (tmp[:-1]+')&')
    print(txt[:-1])


# -

solve6('test001.txt')

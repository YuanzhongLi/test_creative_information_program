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

# +
# (1
parse1obj = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3
}

def FtoT(f):
    f = str(f)
    ret = 0
    for i in range(0, len(f)):
        idx = len(f) - i - 1
        ret += parse1obj[f[idx]] * (4**(i))
        
    return ret


# -

FtoT(123)

# +
# (2
parse2obj = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7
}

def EtoT(e):
    ret = 0
    for i in range(0, len(e)):
        idx = len(e) - i - 1
        ret += parse2obj[e[idx]] * (8**(i))
        
    return ret


# -

EtoT('bcd')

# +
# (3
# ans. 3737

# +
# (4
dict4 = {
    'I': 1,
    'V': 5, 
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

dict4_1 = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}

# ruturn bool
def is_reverse(cur_ch, next_ch):
    if (cur_ch == 'I'):
        return next_ch == 'V' or next_ch == 'X'
    if (cur_ch == 'X'):
        return next_ch == 'L' or next_ch == 'C'
    if (cur_ch == 'C'):
        return next_ch == 'D' or next_ch == 'M'
    return False

def parser4(rome):
    ret = 0
    i = 0
    while (i < len(rome)):
        cur_ch = rome[i]
        if (i < len(rome) - 1):
            next_ch = rome[i + 1]
            if (is_reverse(cur_ch, next_ch)):
                key_str =  cur_ch + next_ch
                ret += dict4_1[key_str]
                i += 2
            else:
                ret += dict4[cur_ch]
                i += 1
        else:
            ret += dict4[cur_ch]
            i += 1
    return ret        


# -

parser4('MCMIV')


# +
# (5
def sub_parser5(num, digit):
    if (digit == 4):
        return 'M' * num
    elif (digit == 3):
        if (num == 9):
            return 'CM'
        elif (num == 4):
            return 'CD'
        elif (num >= 5 and num <= 8):
            return 'D' + 'C' * (num - 5) 
        else:
            return 'C' * num
    elif (digit == 2):
        if (num == 9):
            return 'XC'
        elif (num == 4):
            return 'XL'
        elif (num >= 5 and num <= 8):
            return 'L' + 'X' * (num - 5) 
        else:
            return 'X' * num
    elif (digit == 1):
        if (num == 9):
            return 'IX'
        elif (num == 4):
            return 'IV'
        elif (num >= 5 and num <= 8):
            return 'V' + 'I' * (num - 5) 
        else:
            return 'I' * num

def parser5(t):
    str_t = str(t)    
    for i in range(len(str_t), 4):
        str_t = '0' + str_t
    ret = ''
    for i in range(0, len(str_t)):
        num = int(str_t[i])
        ret += sub_parser5(num, len(str_t) - i)
    return ret


# -

parser5(1904)


# (6
def parser6(t):
    str_t = str(t)    
    for i in range(len(str_t), 4):
        str_t = '0' + str_t
    str_t = str_t[::-1]
    fir_num = int(str_t[0])
    sec_num = int(str_t[1])
    thr_num = int(str_t[2])
    for_num = int(str_t[3])
    if (fir_num == 9):
        if (sec_num == 9):
            if (thr_num == 9):
                return (for_num * 'M' + 'IM')
            elif (thr_num == 4):
                return (for_num * 'M' + 'ID')            
            else:
                return sub_parser5(for_num, 4) + sub_parser5(thr_num, 4) + 'IC'
        elif (sec_num == 4):
            return sub_parser5(for_num, 4) + sub_parser5(thr_num, 3) + 'IL'
        else:
            return sub_parser5(for_nu, 4) + sub_parser5(thr_num, 3) + sub_parser5(sec_num, 2) + 'IX'
    else:
        return parser5(t)               


parser6(149)

# +
# (7
dict7 = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
}

def parser7(s):
    # 番兵追加
    s += ' zero'
    ret = 0
    array_s = s.split()
    if ('thousand' in array_s):
        t_s = ' '.join(array_s)
        t_s = t_s.split('thousand')
        t_0 = t_s[0]
        t_s0 = t_0.split()
        t_1 = t_s[1]
        t_s1 = t_1.split()
        tmp1 = 0
        for i in range(0, len(t_s0)):
            word = t_s0[i]
            tmp1 += dict7[word]
        ret += tmp1 * 1000
        
        if ('hundred' in t_s1):
            h_s = t_1.split('hundred')
            h_0 = h_s[0]
            h_s0 = h_0.split()
            h_1 = h_s[1]
            h_s1 = h_1.split()
            tmp2 = 0
            for j in range(0, len(h_s0)):
                word = h_s0[j]
                tmp2 += dict7[word]
            ret += tmp2 * 100
            
            for k in range(0, len(h_s1)):
                word = h_s1[k]
                ret += dict7[word]
        else:        
            for j in range(0, len(t_s1)):
                word = t_s1[j]
                ret += dict7[word]
    else:            
        for i in range(0, len(array_s)):
            word = array_s[i]
            if (dict7[word] == 100):
                ret *= 100
            else:
                ret += dict7[word]
    return ret        


# -

parser7('fifty four thousand three hundred twelve')



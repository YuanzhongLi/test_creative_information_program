import sys
inp = sys.argv[1]

def get_row_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def make_dic(text):
    n = len(text)
    dic = {}
    key_set = set([])
    for i in range(n - 5):
        si = text[i:i+6]
        if not(si in key_set):
            str_num = str(i)
            str_num = '0' * (3 - len(str_num)) + str_num
            dic[si] = str_num
            key_set.add(si)
    return dic

def solve3(file_path):
    row_text = get_row_text(file_path)
    dic = make_dic(row_text)
    print(dic)

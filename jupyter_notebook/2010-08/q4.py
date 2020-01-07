import sys
inp = sys.argv[1]

def get_row_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def compress_text(text):
    text_array = list(text)
    dic = make_dic(text)
    key_set = set(dic.keys())
    n = len(text)
    j = 0
    memo = []
    while j < n - 5:
        sj = text[j:j+6]
        if sj in key_set:
            v = dic[sj]
            int_v = int(v)
            if int_v == j:
                j += 1
                continue
            tmp = ['9', '9', '9']
            tmp.extend(list(v))
            text_array[j:j+6] = tmp
            j += 6
        else:
            j += 1
    return ''.join(text_array).replace('999', '')

def solve4(file_path):
    row_text = get_row_text(file_path)
    compressed_text = compress_text(row_text)
    print(compressed_text)

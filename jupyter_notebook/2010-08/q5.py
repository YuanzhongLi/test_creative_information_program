import sys
import re
inp = sys.argv[1]

def get_row_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def get_content(text):
    size = len(text)
    ret = ''
    ret += (text * ((6+size-1)//size))
    return ret[:6]

def decode(compressed_text):
    text = compressed_text
    codes = re.findall(r'[0-9]{3}', compressed_text)
    for code in codes:
        m = re.search(code, text)
        i = int(code)
        j = m.span()[0]
        tmp = min(6, j - i)
        rep = get_content(text[i:i+tmp])
        text = text[:j] + rep + text[j+3:]
    return text

def solve5(file_path):
    compressed_text = get_row_text(file_path)
    text = decode(compressed_text)
    print('size: {0}, last10: {1}'.format(len(text), text[-10:]))

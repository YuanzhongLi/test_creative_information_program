import sys
inp = sys.argv[1]

import re

def get_row_text(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def get_compressions(text):
    return re.findall(r'[0-9]{3}', text)

def solve2(file_path):
    row_text = get_row_text(file_path)
    compressions = get_compressions(row_text)
    print(len(compressions))

solve2(inp)

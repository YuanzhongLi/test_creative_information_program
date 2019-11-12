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
file_path = 'image1.txt'
def solve(file_path):
    with open(file_path, mode='r') as f:
        content =  f.read()
        print(content)



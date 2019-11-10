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

def isNumber(s):
    try:
        return type(int(s)) == int  
    except:
        try:
            return type(float(s)) == float
        except:
            return False


def STRtoNumber(s):
    if (isNumber(s)):
        try:
            return int(s)
        except:
            return float(s)
    else:
        return False

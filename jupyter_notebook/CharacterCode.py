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

# 16進数bytes文字列(str)に変換
import binascii
def Hexbytes2Str(hexbytes):
    return binascii.unhexlify(hexbytes).decode('utf-8')


# +
# print(Hexbytes2Str(b'e38193e38293e381abe381a1e381af'))
# こんにちは
# -

# ascii文字列(str)を16進数bytesに変換
def AsciiStr2Hexbytes(string):
    return binascii.b2a_hex(string.encode('utf-8'))


# +
# print(AsciiStr2Hexbytes('Hello'))
# b'48656c6c6f'
# -

# ascii文字列(str)を10進数intに変換
def AsciiStr2Int(asciistring, option='little'):
    return int.from_bytes(asciistring.encode(encoding='ascii'), option)


# +
# print(AsciiStr2Int('a'), AsciiSTR2INT('abc'))
# -

# 10進数をn_bytesの16進数bytesに変換
def Int2hexbytes(intnum, n_bytes=1, option='little'):
    return binascii.hexlify((intnum).to_bytes(n_bytes, option))


# +
# print(Int2hexbytes(97), Int2hexbytes(97, 2, 'little'))
# -

def Int2Char(intnum):
    return Hexbytes2Str(Int2hexbytes(intnum))

# +
# Int2Char(32)

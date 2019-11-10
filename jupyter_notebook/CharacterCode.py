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

# 16進数asciiを文字列(str)に変換
import binascii
def HexAsciiToSTR(hexasciicode):
    return binascii.unhexlify(hexasciicode.encode('ascii')).decode('utf-8')


print(HexAsciiToSTR('e38193e38293e381abe381a1e381af'))


# 文字列(str)を16進数asciiに変換
def STRtoHexAscii(string):
    return binascii.b2a_hex(string.encode('utf-8'))


print(STRtoHexAscii('Hello'))



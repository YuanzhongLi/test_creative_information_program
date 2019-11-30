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
# terminalからの入力をEnterせずに逐次取得しintで返す(ex. a => 97)

import fcntl
import termios
import sys
import os

def getkey():
    fno = sys.stdin.fileno()

    #stdinの端末属性を取得
    attr_old = termios.tcgetattr(fno)

    # stdinのエコー無効、カノニカルモード無効
    attr = termios.tcgetattr(fno)
    attr[3] = attr[3] & ~termios.ECHO & ~termios.ICANON # & ~termios.ISIG
    termios.tcsetattr(fno, termios.TCSADRAIN, attr)

    # stdinをNONBLOCKに設定
    fcntl_old = fcntl.fcntl(fno, fcntl.F_GETFL)
    fcntl.fcntl(fno, fcntl.F_SETFL, fcntl_old | os.O_NONBLOCK)

    chr = 0

    try:
        # キーを取得
        c = sys.stdin.read(1)
        if len(c):
            while len(c):
                chr = (chr << 8) + ord(c)
                c = sys.stdin.read(1)
    finally:
        # stdinを元に戻す
        fcntl.fcntl(fno, fcntl.F_SETFL, fcntl_old)
        termios.tcsetattr(fno, termios.TCSANOW, attr_old)

    return chr

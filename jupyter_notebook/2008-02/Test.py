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

import sys
sys.path.append('..')

import numpy as np

# +
from collections import deque

class Order(object):
    def __init__(self, no, s, e, at):
        self.no = no
        self.s = s
        self.e = e
        if (s < e):
            self.vec = 'up'
        else:
            self.vec = 'down'
        self.at = at
        self.wait = None
        self.onb = None
        
    def __repr__(self):
        return 'orderId: {0}, from: {1}, to: {2}, vec: {3}\norderedAt: {4}, wait-time: {5}, onboard-time: {6}'.format(self.no, self.s, self.e, self.vec, self.at, self.wait, self.onb)

# エレベータ    
class Ele(object):
    def __init__(self, allord):
        self.floor = 0
        # stop, move
        self.status = 'stop'
        # close, open
        self.door = 'close'
        # off, up, down
        self.lamp = 'off'
        self.omega = None
        self.member = 0
        self.uf = deque([])
        self.df = deque([])
        self.allord = allord
        self.time = 0
    def __repr__(self):
        return 'floor: {0}, member: {6}, status: {1}, door: {2}, lamp: {3}, omega: {4}\nplan: {5}'.format(self.floor, self.status, self.door, self.lamp, self.omega, self.plan, self.member)    

    def update(self, floor, status, door, lamp, omega, member):
        orders = []
        while (ordIdx < len(allord) and allord[ordIdx].at == self.time):
            orders.append(allord[ordIdx])
        if len(orders) > 0:
            
        
# -

a = Order(1, 2, 3, 4)
a



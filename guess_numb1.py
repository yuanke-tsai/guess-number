#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:49:47 2021

@author: yuanke.tsai
"""

import random

r = random.randint(1, 100)
count = 1

while True:
    guess = input('請猜一個數字')
    guess = int(guess)
    if guess == r:
        print('你猜對了答案是：', r)
        print('猜了', count + 1, '次')
        break
    else:
        print('你猜錯了！')
        if r > guess:
            print('猜大一點')
        else:
            print('猜小一點')
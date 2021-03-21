#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 19:49:47 2021

@author: yuanke.tsai
"""

import random

r = random.randint(1, 100)
count = 0 #還沒開始，所以數猜幾次為0次
wrong = 0 #還沒開始，所以錯誤次數為0次

#print(r) #檢視是否程式正確時，需執行此行！

while True:
    guess = input('請猜一個數字：')
    guess = int(guess)
    wrong = wrong + 1 #錯誤次數＝起始錯誤次數＋1
    if guess == r:
        print('\n'+'你猜對了答案是：', r)
        count += wrong # c = c + w 之意：次數＝起始次數＋錯誤次數
        print('共猜了', count, '次')
        break
    else:
        print('\n'+'你猜錯了！')
        if r > guess:
            print('猜大一點')
        else:
            print('猜小一點')
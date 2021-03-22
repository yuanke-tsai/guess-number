# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#上下界自行定義 + 輸入範圍錯誤提示（輸入範圍錯誤，不列入猜測次數！）

import random

guess_low = int(input('請輸入下界：'))
guess_upper = int(input('請輸入上界：'))

r = random.randint(guess_low, guess_upper)
count = 0 #還沒開始，所以數猜幾次為0次
wrong = 0 #還沒開始，所以錯誤次數為0次
rang_w = 0 #輸入範圍錯誤，起始次數為0次

print('測試中答案：', r) #檢視是否程式正確時，需執行此行！

while True:
    guess = int(input('請猜一個數字：'))
    wrong = wrong + 1#錯誤次數＝起始錯誤次數＋1
    if guess == r:
        print('\n'+'你猜對了答案是：', r)
        count += wrong - rang_w # c = c + w 之意：次數＝起始次數＋錯誤次數
        print('共猜了', count, '次')
        break
    else:
        while True:
            if guess < guess_low:
                rang_w = rang_w + 1 #如何解釋？
                print('輸入值未在範圍內！！')
                break    
            else:
                if r > guess:
                    print('\n'+'你猜錯了，猜大一點')
                else:
                    print('\n'+'你猜錯了，猜小一點')
            break
                            
                
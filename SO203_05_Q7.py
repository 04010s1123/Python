#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
プログラミング基礎Python
制御構文
練習問題7
P.16「内包表記」のソースコードを以下に変更してください。
    1, 1, 2, 3, 5, 8, 13, 21

静的解析ツール
================
>>> pycodestyle SO203_05_Q7.py
================

実行例
================
>>> python SO203_05_Q7.py
[1, 1, 4, 9, 25, 64, 169, 441]
[1, 1, 4, 9, 25, 64, 169, 441]
================

'''


# ここより下に解答を記載する。
num_list = [1, 1, 2, 3, 5, 8, 13, 21]
num_list_1 = []
for num in num_list:
	num_list_1.append(num ** 2)
print(num_list_1)

num_list_2 = [x ** 2 for x in num_list]
print(num_list_2)

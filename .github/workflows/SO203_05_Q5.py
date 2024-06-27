#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
プログラミング基礎Python
制御構文
練習問題5
P.11「break文」のソースコードを以下に変更してください。
    5, 6, 7, 8, 9

静的解析ツール
================
>>> pycodestyle SO203_05_Q5.py
================

実行例
================
>>> python SO203_05_Q5.py
5
================

'''


# ここより下に解答を記載する。
num_list = [5, 6, 7, 8, 9]
for num in num_list:
	if num % 2 == 0:
		break
	print(num)

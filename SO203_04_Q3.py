#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
プログラミング基礎Python
演算子
練習問題3
以下の文字列を表示してください。
    2つの文字列「Good」と「Morning」を結合した文字列
    「OK!!」を5回繰り返した文字列

静的解析ツール
================
>>> pycodestyle SO203_04_Q3.py
================

実行例
================
>>> python SO203_04_Q3.py
GoodMorning
OK!!OK!!OK!!OK!!OK!!
================

'''


# ここより下に解答を記載する。
print('Good' + 'Morning')
int_1 = 1
while int_1 <= 5:
	print('OK!!', end='')
	int_1 += 1
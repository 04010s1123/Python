#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
プログラミング基礎Python
関数とモジュール
練習問題2.
P.8「ユーザ定義関数」のソースコードを変更して、以下の結果を表示してください。
    7.8 + 3.4

静的解析ツール
================
>>> pycodestyle SO203_06_Q2.py
================

実行例
================
>>> python SO203_06_Q2.py
11.2
================

'''


# ここより下に解答を記載する。
def calc(num1, num2):
	x = num1 + num2
	return x

num = calc(7.8, 3.4)
print(num)

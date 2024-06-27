#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
プログラミング基礎Python
関数とモジュール
練習問題3
練習問題2に、「引き算した結果を返す関数」を追加して、以下の結果を表示してください。
    7.8 - 3.4

静的解析ツール
================
>>> pycodestyle SO203_06_Q3.py
================

実行例
================
>>> python SO203_06_Q3.py
4.4
================

'''


# ここより下に解答を記載する。
def Calc(num1, num2):
	x = num1 + num2
	return x

def Subt(num1, num2):
	x =  num1 - num2
	return x

num = Subt(7.8, 3.4)
print(num)

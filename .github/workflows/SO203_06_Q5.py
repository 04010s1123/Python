#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
プログラミング基礎Python
関数とモジュール
練習問題5
外部ライブラリの数学関数を使用して、以下を表示してください。
    21の平方根を小数点以下3桁まで

静的解析ツール
================
>>> pycodestyle SO203_06_Q5.py
================

実行例
================
>>> python SO203_06_Q5.py
4.583
================

'''


# ここより下に解答を記載する。
import math
def  Sqrt(num1, num2):
#num1:平方根を求める対象値/num2:表数点以下表記数
	print(f'{math.sqrt(num1):.{num2}f}') 
#	return  round(math.sqrt(num1),num2)

Sqrt(21, 3)

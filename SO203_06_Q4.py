#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
プログラミング基礎Python
関数とモジュール
練習問題4.
P.10「モジュール」のソースコードを以下に変更してください。
    num1 = -2.4

静的解析ツール
================
>>> pycodestyle SO203_06_Q4.py
================

実行例
================
>>> python SO203_06_Q4.py
2.4
================

'''


# ここより下に解答を記載する。
import math

num1 = -2.4
num2 = math.fabs(num1)
print(num2)

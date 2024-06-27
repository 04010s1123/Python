#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
プログラミング基礎Python
関数とモジュール
練習問題
P.5「組み込み関数」のソースコードを作成してください。

静的解析ツール
================
>>> pycodestyle SO203_06_Q1.py
================

実行例
================
>>> python SO203_06_Q1.py < SO203_06_Q1_input.txt
何か入力してください。＞「おはようございます。」は、10文字です。
「おはようございます。」は、10文字です。
「おはようございます。」は、10文字です。
================

'''


# ここより下に解答を記載する。
import sys
with open( 'SO203_06_Q1_input.txt', encoding='utf-8') as f:
	file_txt = f.read()
txt = input('何か入力してください>')
if len(txt) == 0:
	txt = file_txt
	txt_len = len(txt)
else:
	txt_len = len(txt)
print('「%s」は、%d文字です。' % (txt, txt_len)) 
print('「{}」は、{}文字です。'.format(txt, txt_len))
print(f'「{txt}」は、{txt_len}文字です。')

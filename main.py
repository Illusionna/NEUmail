'''
# System --> Windows & Python3.10.0
# File ----> main.py
# Author --> Illusionna
# Create --> 2024/03/22 09:23:21
'''
# -*- Encoding: UTF-8 -*-

# Python 3.10.0+ 建议.
# pip install alive-progress
# pip install flask
# 优先编译 gcc ./utils/scan.c -o ./utils/scan.exe 生成依赖文件.

import os
import utils.inherit as inherit


if __name__ == '__main__':
    print('\033[H\033[J', end='')
    os.system('')
    inherit.SCAN()
    inherit.PROOFREAD()
    inherit.GUIDE()
    inherit.USAGE()
    # input('按 Enter 退出...')
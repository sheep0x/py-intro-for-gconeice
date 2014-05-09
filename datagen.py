#! /usr/bin/env python
# encoding: UTF-8

# To the extent possible under law, Chen Ruichao has waived all copyright and
# related or neighboring rights to this work.

from random import randint

# N 为 1~100 之间的随机整数
T = randint(1, 50000)
print T

# i 取 0, 1, 2, ..., T-1
for i in range(T):
    print randint(1, 2**23-1)

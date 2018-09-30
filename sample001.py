# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 使用了for循环，打印，数组，判断

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print(i, j, k)
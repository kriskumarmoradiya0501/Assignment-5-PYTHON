# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:06:16 2024

@author: ADMIN
"""

def multiplication_table(n, upto=10):
    return {i: n * i for i in range(1, upto + 1)}

print(multiplication_table(5))  
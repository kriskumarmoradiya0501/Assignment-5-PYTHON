# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:06:51 2024

@author: ADMIN
"""

def common_keys(d1, d2):
    return list(set(d1.keys()) & set(d2.keys()))

d1 = {'a': 100, 'b': 200}
d2 = {'b': 300, 'c': 400}
print(common_keys(d1, d2)) 
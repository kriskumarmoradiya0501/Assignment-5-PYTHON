# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:06:34 2024

@author: ADMIN
"""

def key_with_highest_value(d):
    return max(d, key=d.get)

d = {'a': 100, 'b': 300, 'c': 200}
print(key_with_highest_value(d))  
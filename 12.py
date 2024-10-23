# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:06:43 2024

@author: ADMIN
"""

def sort_dict_by_values(d):
    return sorted(d.items(), key=lambda item: item[1])

d = {'a': 100, 'b': 300, 'c': 200}
print(sort_dict_by_values(d)) 
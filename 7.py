# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:05:55 2024

@author: ADMIN
"""

def remove_duplicates(lst):
    return list(set(lst))

lst = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(lst))  
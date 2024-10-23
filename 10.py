# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:06:26 2024

@author: ADMIN
"""

def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]
print(list_intersection(lst1, lst2)) 
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:05:29 2024

@author: ADMIN
"""

def average(lst):
    return sum(lst) / len(lst) if lst else 0

numbers = [10, 20, 30, 40, 50]
print(average(numbers)) 
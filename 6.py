# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:05:43 2024

@author: ADMIN
"""

def longest_string(lst):
    return max(lst, key=len) if lst else None

strings = ["apple", "banana", "cherry", "watermelon"]
print(longest_string(strings)) 
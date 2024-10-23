# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:05:08 2024

@author: ADMIN
"""

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("Hello World"))
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:06:06 2024

@author: ADMIN
"""

def char_frequency(s):
    return {char: s.count(char) for char in set(s)}

print(char_frequency("hello world"))  